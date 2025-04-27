import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))
from models.wake_word_model import WakeWordModel


class TestWakeWordModel(unittest.TestCase):

    @patch('models.wake_word_model.vision.GestureRecognizer.create_from_options')
    def test_init_recognizer(self, mock_create):

        mock_create.return_value = MagicMock()

        model = WakeWordModel()

        self.assertIsNotNone(model.recognizer)
        mock_create.assert_called_once()

    @patch('models.wake_word_model.mp.Image')
    @patch('models.wake_word_model.WakeWordModel.init_recognizer')
    def test_gesture_recognition(self, mock_init, mock_image):
        mock_recognizer = MagicMock()
        mock_recognizer.recognize.return_value.gestures = [MagicMock(category_name="Thumb_Up")]
        mock_init.return_value = None

        model = WakeWordModel()
        model.recognizer = mock_recognizer

        result = model.gesture_recognition(mock_image)
        self.assertEqual(result.category_name, "Thumb_Up")

    @patch('models.wake_word_model.Camera')
    @patch('models.wake_word_model.mp.solutions.hands.Hands')
    def test_detecting_gestures(self, mock_hands, mock_camera):
        mock_camera_instance = MagicMock()
        mock_camera_instance.get_success = True
        mock_camera_instance.capture.return_value = None
        mock_camera_instance.get_frame.return_value = MagicMock()
        mock_camera.return_value = mock_camera_instance

        mock_hands_instance = MagicMock()
        mock_hands.return_value.__enter__.return_value = mock_hands_instance

        model = WakeWordModel()
        model.detecting_gestures()

        mock_camera_instance.capture.assert_called()
        mock_hands_instance.process.assert_called()

if __name__ == '__main__':
    unittest.main()