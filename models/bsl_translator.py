import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
import numpy as np
import tensorflow as tf
from transformers import pipeline
from PIL import Image

class SignLanguageRecogniser():
    def __init__(self):
        self.listeningState = False

        self.camera = Camera()

        #self.pipe = pipeline("image-classification", model="Heem2/sign-language-classification")
        
        # try:
        #     self.model = tf.keras.models.load_model('C:/Users/abbie/Desktop/Star/models/alpha_sign4.h5')
        # except Exception as e:
        #     print(e)

        try:
            self.model = tf.keras.models.load_from_json('C:/Users/abbie/Desktop/Star/models/model.json')
            self.model.load_weights('C:/Users/abbie/Desktop/Star/models/model.h5')
        except Exception as e:
            print(e)

        self.request = []
        # self.translations = ['A','B','C','D','E','F','G','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def preprocess_image(self, image):
        # image = self.camera.resize(image, 64, 64)
        # image_array = np.array(image)
        # image_array = np.expand_dims(image_array, axis=0)

        image = self.camera.recolour(image)
        
        self.predict(Image.fromarray(image))

    def predict(self, image):
        self.request.append((self.model.predict(np.expand_dims(image, axis=0))[0]))

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