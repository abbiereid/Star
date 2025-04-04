import keras
from keras import ops
import os
import sys

LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXY"


class Classifier:
    def __init__(self):
        self.model = keras.models.load_model("C:/Users/abbie/Desktop/dissertation/Star/models/model6.keras")

    def classify(self, points):
        predictions = self.model.predict(points[:, :, :2], verbose=0)
        prediction = ops.argmax(predictions, -1)
        probability = predictions[0][prediction[0]]
        letter = LETTERS[prediction[0]]

        return letter, probability
