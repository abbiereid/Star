import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from observer import IObserver
from models.wake_word_model import WakeWordModel
import numpy as np
import tensorflow as tf

class SignLanguageRecogniser(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

        self.camera = Camera()
        try:
            self.model = tf.keras.models.load_model('C:/Users/abbie/Desktop/Star/models/alpha_sign4.h5')
        except Exception as e:
            print(e)

        self.request = []
        self.translations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        

    def notify(self, *args, **kwargs):
        self.listeningState = kwargs.get('state', False)
        if self.listeningState:
            self.record_request()
        else:
            self.camera.stop_recording()
        

    def preprocess_image(self, image):
        image = self.camera.resize(image, 64, 64)
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)

        self.predict(image_array)

    def predict(self, image):
        self.request.append(self.translations[np.argmax(self.model.predict(image))])

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
