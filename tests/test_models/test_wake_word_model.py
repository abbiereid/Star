import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))
from models.wake_word_model import WakeWordModel
import numpy as np

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
        mock_gesture = MagicMock()
        mock_gesture.category_name = "Thumb_Up"
        mock_recognizer.recognize.return_value.gestures = [[mock_gesture]]
        mock_init.return_value = None

        model = WakeWordModel()
        model.recognizer = mock_recognizer

        result = model.gesture_recognition(mock_image)
        self.assertEqual(result.category_name, "Thumb_Up")
        
if __name__ == '__main__':
    unittest.main()