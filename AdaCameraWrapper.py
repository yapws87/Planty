import base64
from picamera2 import PiCamera2
from io import BytesIO
import time


# Set up camera
cam = PiCamera2()
cam.resolution = (1920,1080)
time.sleep(2)

def capture():
    # Capture image to in-memory stream
    stream = BytesIO()
    cam.capture(stream,format='jpeg')
    stream.seek(0)

    # convert to base64
    encoded_str = base64.b64encode(stream.getvalue()).decode('utf-8')
    return encoded_str