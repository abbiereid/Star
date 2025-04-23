import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.camera import Camera
from models.slr_utils.ASLrecognition import ASLrecognition as ASL
from models.assistant import Assistant
import numpy as np

class SignLanguageRecogniser():
    def __init__(self):
        self.listeningState = False
        self.camera = Camera()
        self.recogniser = ASL()
        self.request = []
        self.assistant = Assistant()

    def preprocess_image(self, image):
        image = self.camera.resize(image, 256, 256)
        self.predict(np.array(image))

    def predict(self, image):
        prediction = self.recogniser.processImage(image)

        if prediction is not None:
            self.request.append(prediction)

    def record_request(self):
            self.listeningState = True
            self.title = "Sign Language Translator"
            while self.listeningState:
                self.camera.capture()
                self.camera.show(self.camera.get_frame(), str(self.request[-1]) if self.request else "No Gesture Detected", self.title)
                self.preprocess_image(self.camera.get_frame())
            self.camera.release_window(self.title)

    def stop_recording(self):
        self.listeningState = False
        if self.request:
            return self.send_request()

    def send_request(self):
        formedRequest = ""
        for letter in self.request:
            formedRequest = formedRequest + letter[0]
        self.request = []

        if formedRequest != "":
            print("Sending request: ", formedRequest)
            return self.assistant.recieveRequest(formedRequest)
        else:
            print("Request is empty")