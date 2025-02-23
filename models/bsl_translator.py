import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from observer import IObserver
import numpy as np
import tensorflow as tf

class SignLanguageRecogniser(IObserver):
    def __init__(self):
        self.camera = Camera()
        try:
            self.model = tf.keras.models.load_model('C:/Users/abbie/Desktop/Star/models/alpha_sign4.h5')
        except Exception as e:
            print(e)
        self.request = []
        

    def notify():
        pass

    def preprocess_image(self, image):
        image = self.camera.resize(image, 64, 64)
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        
        self.predict(image_array)

    def predict(self, image):
        prediction = self.model.predict(image)
        self.request.append(prediction)

    def record_request(self):
        self.camera.record()
        while self.camera.recording:
            self.camera.capture()
            self.camera.show(self.camera.get_frame())
            self.preprocess_image(self.camera.get_frame())
        self.send_request()

    def send_request(self):
        print(self.request)
        self.request = []
    
    def send_results(self):
        pass

slr = SignLanguageRecogniser()
slr.record_request()
