import os
import sys
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from slr_utils.recognition import IRecognition

# Misrecogntion fixes credited to https://github.com/kevinjosethomas

class ASLrecognition(IRecognition):
    def __init__(self, min_confidence: float = 0.8):
        self.model_path = "C:/Users/abbie/Desktop/dissertation/Star/models/model6.keras"
        self.gestures = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                        "U", "V", "W", "X", "Y"]
        super().__init__(self.model_path, min_confidence, self.gestures)

    def fix_misrecognition(self, gesture: str, points: np.ndarray, hand: str):
        if gesture in ["A", "T"]:
            thumb_tip = points[0][4]
            thumb_middle = points[0][3]
            index_tip = points[0][8]
            if hand == "left":
                if thumb_tip[0] > index_tip[0] and thumb_middle[0] > index_tip[0]:
                    gesture = "A"
                else:
                    gesture = "T"
            else:
                if thumb_tip[0] < index_tip[0] and thumb_middle[0] < index_tip[0]:
                    gesture = "A"
                else:
                    gesture = "T"

        # if letter == "K":
        #     index_tip = points[0][8]
        #     index_middle = points[0][7]
        #     middle_tip = points[0][12]
        #     middle_middle = points[0][11]

        #     if index_tip[1] < index_middle[1] or middle_tip[1] < middle_middle[1]:
        #         print(index_tip[1], index_middle[1], middle_tip[1], middle_middle[1])
        #         letter = "I"

        if gesture in ["D", "I"]:
            index_tip = points[0][8]
            pinky_tip = points[0][20]

            if index_tip[1] > pinky_tip[1]:
                gesture = "I"
            else:
                gesture = "D"

        if gesture in ["F", "W"]:
            index_tip = points[0][8]
            pinky_tip = points[0][20]

            if index_tip[1] > pinky_tip[1]:
                gesture = "F"
            else:
                gesture = "W"

        return gesture