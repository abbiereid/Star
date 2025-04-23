import numpy as np
import keras
from keras import ops
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.slr_utils.landmarker import Landmarker

class IRecognition():
    def __init__(self, model_path ,min_confidence: float = 0.8, gestures: list = []):
        self.min_confidence = min_confidence
        self.landmarker = Landmarker()
        self.gestures = gestures
        self.model = keras.models.load_model(model_path)
        self.predictions = []

    def processImage(self, image: np.ndarray):
        success, image, points, first_landmark, hand = self.landmarker.draw_landmarks(
            image
        )

        if not success:
            return None
        
        if success:
            if self.gestures != []:
                try:
                    gesture, probability = self.classifyGesture(points)
                    gesture = self.fix_misrecognition(gesture, points, hand)

                    if probability > self.min_confidence:
                        self.predictions.append(gesture)

                        if len(self.predictions) > 1:
                            if len(self.predictions) < 10:
                                return

                            if len(set(self.predictions[-10:])) == 1:
                                gesture = self.predictions[-1]
                                self.predictions = []
                                return gesture, round(probability * 100 * 100) / 100
                    
                except Exception as e:
                        print(f"Error: {e}")
                        return None
            else:
                gesture = None
                return gesture, None
            
    def classifyGesture(self, points: np.ndarray):
        predictions = self.model.predict(points[:, :, :2], verbose=0)
        prediction = ops.argmax(predictions, -1)
        probability = predictions[0][prediction[0]]
        gesture = self.gestures[prediction[0]]

        return gesture, probability
    
    def fix_misrecognition(self, gesture: str, points: np.ndarray, hand: str):
        pass