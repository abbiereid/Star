import cv2
import threading
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from slr_utils.landmarker import Landmarker
from slr_utils.classifier import Classifier

class Recognition:

    def __init__(self, min_confidence: float = 0.80):
        self.min_confidence = min_confidence
        self.landmarker = Landmarker()
        self.classifier = Classifier()

    def process(self, image: np.ndarray):

        success, image, points, first_landmark, hand = self.landmarker.draw_landmarks(
            image
        )

        if not success:
            return None
        
        # If a hand is detected in the frame
        if success:
            try:
                letter, probability = self.classifier.classify(points)
                letter = self.fix_misrecognition(letter, points, hand)

                # Ensure the alphabet classification probability is larger than the minimum confidence
                if probability > self.min_confidence:
                    return letter, round(probability * 100 * 100) / 100
            except Exception as e:
                    print(f"Error: {e}")
                    return None

    def fix_misrecognition(self, letter: str, points: np.ndarray, hand: str):

        if letter in ["A", "T"]:
            thumb_tip = points[0][4]
            thumb_middle = points[0][3]
            index_tip = points[0][8]
            if hand == "left":
                if thumb_tip[0] > index_tip[0] and thumb_middle[0] > index_tip[0]:
                    letter = "A"
                else:
                    letter = "T"
            else:
                if thumb_tip[0] < index_tip[0] and thumb_middle[0] < index_tip[0]:
                    letter = "A"
                else:
                    letter = "T"

        # if letter == "K":
        #     index_tip = points[0][8]
        #     index_middle = points[0][7]
        #     middle_tip = points[0][12]
        #     middle_middle = points[0][11]

        #     if index_tip[1] < index_middle[1] or middle_tip[1] < middle_middle[1]:
        #         print(index_tip[1], index_middle[1], middle_tip[1], middle_middle[1])
        #         letter = "I"

        if letter in ["D", "I"]:
            index_tip = points[0][8]
            pinky_tip = points[0][20]

            if index_tip[1] > pinky_tip[1]:
                letter = "I"
            else:
                letter = "D"

        if letter in ["F", "W"]:
            index_tip = points[0][8]
            pinky_tip = points[0][20]

            if index_tip[1] > pinky_tip[1]:
                letter = "F"
            else:
                letter = "W"

        return letter
