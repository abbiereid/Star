import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from models.slr_utils.recognition import Recognition
import numpy as np
import time

class SignLanguageRecogniser():
    def __init__(self):
        self.listeningState = False
        self.camera = Camera()
        self.recogniser = Recognition()
        self.request = []
        self.lastLetter = None
        self.timeStamp = 0

    def preprocess_image(self, image):
        image = self.camera.resize(image, 256, 256)
        self.predict(np.array(image))

    def predict(self, image):
        prediction = self.recogniser.process(image)

        if prediction is not None:
            if prediction is not self.lastLetter:
                self.request.append(prediction)
                self.timeStamp = time.time()
            if self.timeStamp + 0.5 < time.time():
                self.request.append(prediction)
                self.timeStamp = time.time()
            

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
        for letter in self.request:
            print(letter)
        self.request = []
    
    def send_results(self):
        pass