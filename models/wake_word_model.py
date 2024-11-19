import mediapipe as mp
import cv2
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from mediapipe.tasks import python
import time
from mediapipe.tasks.python import vision

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def gesture_recognition(image):
    try:
        with open('models\gesture_recognizer.task', 'rb') as file:
            model = file_content = file.read()
        base_options = python.BaseOptions(model_asset_buffer=model)
        options = vision.GestureRecognizerOptions(base_options=base_options)
        recognizer = vision.GestureRecognizer.create_from_options(options)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        results = recognizer.recognize(mp_image)

        if results.gestures:
            return results.gestures[0][0]
        else:
            return "No gesture detected"
    except Exception as e:
        print(f"Error in gesture recognition: {e}")
    
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    camera = Camera()

    while camera.get_success:
        camera.capture()
        
        image = cv2.cvtColor(camera.get_frame(), cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False

        print(gesture_recognition(image))

        try:
            results = hands.process(image)
        except Exception as e:
            print(f"Error in hands.process: {e}")
            continue

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        
        camera.show(image)
