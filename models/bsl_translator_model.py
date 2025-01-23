import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
import cv2
from observer import IObserver
#import predict

class SignLanguageRecogniser(IObserver):
    def __init__(self):
        self.camera = Camera()

    def notify():
        pass

    def record_request(self):
        while self.camera.get_success:
            self.camera.capture()
            self.camera.record()
            image = cv2.cvtColor(self.camera.get_frame(), cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            self.camera.show(image)

    def send_request():
        pass

    def send_results():
        pass


#subprocess.run('pip freeze' , shell=True)

#subprocess.run('python -m SLR.slr.predict poseformer_v1.0_bsl.ckpt request.mp4 --batch_size 64 --embedding_kind spatial --video_file_extension mp4 ', shell=True)

slr = SignLanguageRecogniser()
slr.record_request()
