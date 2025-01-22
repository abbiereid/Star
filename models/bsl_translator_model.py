import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera

camera = Camera()
while camera.get_success:
    camera.capture()
    camera.show(camera.get_frame())

