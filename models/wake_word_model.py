import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import sys
import threading
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    camera = Camera()
    capture_thread = threading.Thread(target=camera.capture)
    capture_thread.start()

    while camera.get_running():
        if not camera.get_success():
            continue
        
        image = cv2.cvtColor(camera.get_frame(), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        try:
            results = hands.process(image)
        except Exception as e:
            print(f"Error in hands.process: {e}")
            continue

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print(results)