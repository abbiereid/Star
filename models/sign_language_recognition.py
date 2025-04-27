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
        self.formedRequest = ""

    def preprocess_image(self, image):
        image = self.camera.resize(image, 256, 256)
        self.predict(np.array(image))

    def predict(self, image):
        prediction = self.recogniser.processImage(image)

        if prediction is not None:
            self.request.append(prediction)
            self.formedRequest = self.formedRequest + prediction[0]

    def record_request(self):
            self.formedRequest = ""
            self.request = []
            self.listeningState = True
            self.title = "Sign Language Translator"
            while self.listeningState:
                self.camera.capture()
                self.camera.show(self.camera.get_frame(), str(self.request[-1]) if self.request else "No Gesture Detected", self.title, self.formedRequest)
                self.preprocess_image(self.camera.get_frame())
            self.camera.release_window(self.title)

    def stop_recording(self):
        self.listeningState = False
        if self.request:
            return self.send_request()

    def send_request(self):
        if self.formedRequest != "":
            print("Sending request: ", self.formedRequest)
            return self.assistant.recieveRequest(self.formedRequest)
        else:
            print("Request is empty")