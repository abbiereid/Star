import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from models.wake_word_model import WakeWordModel


class TestWakeWordModel(unittest.TestCase):

    def test_wakeWordModel_notifiesObservers_whenWakePhraseIsUsed(self):
        # Arrange
        model = WakeWordModel()
        observer = MagicMock()
        observer.subscribe(model)
        # Act
        model.notify(state=True)
        # Assert
        assert observer.notify.called()

    def test_wakeWordModel_doesNotNotifyObservers_whenWakePhraseIsNotUsed():
        # Arrange

        # Act

        # Assert
        pass

    def test_wakeWordModel_statesTrue_whenWakePhraseIsUsed():
        # Arrange

        # Act

        # Assert
        pass

    def test_wakeWordModel_statesFalse_whenSleepPhraseIsUsed():
        # Arrange

        # Act

        # Assert
        pass