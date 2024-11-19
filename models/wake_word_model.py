import mediapipe as mp
import cv2
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def gesture_recognition(image):
    return
    

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
        
        print(results)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        
        camera.show(image)
