import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from observer import IObserver

class SignLanguageRecogniser(IObserver):
    def __init__(self):
        self.camera = Camera()
        

    def notify():
        pass

    def record_request(self):
        self.camera.record()
        while self.camera.recording:
            self.camera.capture()
            self.camera.show(self.camera.get_frame())
        self.send_request()

    def send_request(self):
        pass
    
    def send_results(self):
        pass

slr = SignLanguageRecogniser()
slr.send_request()
