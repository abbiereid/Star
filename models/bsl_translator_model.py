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
        pass

    def update():
        pass

    def record_request():
        pass

    def send_request():
        pass

    def send_results():
        pass


#subprocess.run('pip freeze' , shell=True)

#subprocess.run('python -m SLR.slr.predict poseformer_v1.0_bsl.ckpt request.mp4 --batch_size 64 --embedding_kind spatial --video_file_extension mp4 ', shell=True)