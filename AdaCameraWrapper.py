import base64
#from picamera2 import PiCamera2
from io import BytesIO
import time
import subprocess


# Set up camera
#cam = PiCamera2()
#cam.resolution = (1920,1080)
#time.sleep(2)
cam_width = 640
cam_height = 480

def capture(file_name):
    # Capture image to in-memory stream
    #stream = BytesIO()
    #cam.capture(stream,format='jpeg')
    #stream.seek(0)
    encoded_str = ""
    image_path = file_name#"capture.jpg"
    subprocess.run(["libcamera-still","-o",image_path, "--width", str(cam_width), "--height", str(cam_height)])
    #time.sleep(2)
    with open(image_path, "rb") as image_file:
        encoded_str = base64.b64encode(image_file.read()).decode('utf-8')

    # convert to base64
    #encoded_str = base64.b64encode(stream.getvalue()).decode('utf-8')
    return encoded_str