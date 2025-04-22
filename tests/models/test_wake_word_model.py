import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from models.wake_word_model import WakeWordModel

class TestWakeWordModel(unittest.TestCase):
    pass