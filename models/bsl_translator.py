import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from observer import IObserver
from keras.models import load_model


class SignLanguageRecogniser(IObserver):
    def __init__(self):
        self.camera = Camera()
        self.model = load_model('models/alpha_sign.h5')
        self.request = []
        

    def notify():
        pass

    def preprocess_image(self, image):
        pass

    def predict(self, image):
        pass

    def record_request(self):
        self.camera.record()
        while self.camera.recording:
            self.camera.capture()
            self.camera.show(self.camera.get_frame())
            self.predict(self.camera.get_frame())
        self.send_request()

    def send_request(self):
        self.request = []
    
    def send_results(self):
        pass

slr = SignLanguageRecogniser()

