import subprocess
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from camera import Camera
#import predict

camera = Camera()
while camera.get_success:
    camera.capture()
    camera.show(camera.get_frame())

subprocess.run('python -m SLR.slr.predict poseformer_v1.0_bsl.ckpt request.mp4 --batch_size 64 --embedding_kind spatial --video_file_extension mp4 ', shell=True)