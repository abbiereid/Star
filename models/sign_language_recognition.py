import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from models.slr_utils.recognition import Recognition
import numpy as np
import cv2

class SignLanguageRecogniser():
    def __init__(self):
        self.listeningState = False

        self.camera = Camera()

        self.recogniser = Recognition()

        self.request = []

    def preprocess_image(self, image):
        image = cv2.resize(image, (256, 256))
        self.predict(np.array(image))

    def predict(self, image):
        prediction = self.recogniser.process(image)

        self.request.append(prediction)

    def record_request(self):
            self.listeningState = True
            while self.listeningState:
                self.camera.capture()
                self.camera.show(self.camera.get_frame(), str(self.request[-1]) if self.request else "No Gesture Detected", "Sign Language Translator")
                self.preprocess_image(self.camera.get_frame())

    def stop_recording(self):
        self.listeningState = False
        if self.request:
            self.send_request()

    def send_request(self):
        print(self.request)
        self.request = []
    
    def send_results(self):
        pass

