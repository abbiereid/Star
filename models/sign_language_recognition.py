import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
import numpy as np
import tensorflow as tf
from PIL import Image

class SignLanguageRecogniser():
    def __init__(self):
        self.listeningState = False

        self.camera = Camera()

        self.request = []
        self.translations = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def preprocess_image(self, image):
        image = self.camera.resize(image, 21, 3)
        image = self.camera.recolour(image)
        
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        
        self.predict(Image.fromarray(image))

    def predict(self, image):
        self.request.append()

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

slr = SignLanguageRecogniser()
slr.record_request()

