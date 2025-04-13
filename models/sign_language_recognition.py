import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from assistant import Assistant
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

        self.assistant = Assistant()

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
        formedRequest = ""
        for letter in self.request:
            formedRequest = formedRequest + letter[0]
        self.request = []

        if formedRequest is not "":
            self.assistant.receive_request(formedRequest)
        else:
            print("Request is empty")
    
    def send_results(self):
        pass