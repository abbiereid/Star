import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..','..'))
from models.assistant import Assistant

class TestAssistant(unittest.TestCase):
    
    def setUp(self):
        self.assistant = Assistant()

    @patch('models.assistant.Assistant.processRequest')
    def test_preprocess_request(self, mock_process_request):
        mock_process_request.return_value = "Processed request"
        request = "Turn on the lights"
        response = self.assistant.preprocessRequest(request)
        
        mock_process_request.assert_called_once()
        self.assertEqual(response, "Processed request")

if __name__ == '__main__':
    unittest.main()