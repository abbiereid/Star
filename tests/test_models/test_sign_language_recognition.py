import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))
from models.sign_language_recognition import SignLanguageRecogniser as slr
import numpy as np

class TestSignLanguageRecognition(unittest.TestCase):

    @patch('keras.models.load_model')
    @patch('utils.camera.Camera.resize')
    @patch('models.sign_language_recognition.SignLanguageRecogniser.predict')
    def test_preprocess_image(self, mock_predict, mock_camera_resize, mock_load_model):
        mock_image = MagicMock()
        mock_resized_image = MagicMock()
        mock_camera_resize.return_value = mock_resized_image
        mock_predict.return_value = "mock_prediction"
        mock_load_model.return_value = MagicMock()

        with patch('numpy.array', return_value="mock_array") as mock_np_array:
            mock_predict.return_value = "mock_prediction"

            slr_instance = slr()
            slr_instance.preprocess_image(mock_image)

            mock_camera_resize.assert_called_once_with(mock_image, 256, 256)
            mock_predict.assert_called_once_with(np.array(mock_resized_image))

    @patch('models.slr_utils.recognition.IRecognition')
    def test_predict(self, mock_recogniser):
        mock_image = MagicMock()
        mock_prediction = ["mock_prediction"]
        mock_recogniser.processImage.return_value = mock_prediction

        slr_instance = slr()
        slr_instance.recogniser = mock_recogniser
        slr_instance.request = []
        slr_instance.formedRequest = ""

        slr_instance.predict(mock_image)

        mock_recogniser.processImage.assert_called_once_with(mock_image)
        self.assertEqual(slr_instance.request, [mock_prediction])
        self.assertEqual(slr_instance.formedRequest, "mock_prediction")

    # def test_record_request(self):
    #     pass

    def test_stop_recording(self):
        slr_instance = slr()
        slr_instance.listeningState = True
        slr_instance.request = ["mock_request"]

        result = slr_instance.stop_recording()

        self.assertFalse(slr_instance.listeningState)

    @patch('models.assistant.Assistant.receiveRequest')
    def test_send_request(self, mock_receive_request):
        mock_receive_request.return_value = "mock_response"

        slr_instance = slr()
        slr_instance.formedRequest = "mock_request"

        result = slr_instance.send_request()

        mock_receive_request.assert_called_once_with("mock_request")
        self.assertEqual(result, "mock_response")

if __name__ == '__main__':
    unittest.main()