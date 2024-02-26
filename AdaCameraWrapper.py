import base64
#from picamera2 import PiCamera2
from io import BytesIO
import time
import subprocess
from PIL import Image


# Set up camera
#cam = PiCamera2()
#cam.resolution = (1920,1080)
#time.sleep(2)
cam_width = 1920
cam_height = 1080

def convert2str(input_path, width, height):
    # Read the image
    img = Image.imread(input_path)
    
    # Resize the image
    resized_image = img.resize(height, width)

    # Convert resized image to bytes
    with BytesIO() as buffer:
        resized_image.save(buffer, format="JPEG")
        image_byte = buffer.getvalue()

    encoded_str = base64.b64encode(image_byte).decode('utf-8')
    # Save the resized image
    #imageio.imwrite(output_path, resized_image)
    return encoded_str

def capture(file_name):
    # Capture image to in-memory stream
    #stream = BytesIO()
    #cam.capture(stream,format='jpeg')
    #stream.seek(0)
    encoded_str = ""
    image_path = file_name#"capture.jpg"
    subprocess.run(["libcamera-still","-o",image_path, "--width", str(cam_width), "--height", str(cam_height)])
    #time.sleep(2)

    encoded_str = convert2str(image_path,320,240)
    # with open(image_path, "rb") as image_file:
    #     image_byte = resize_image(image_path,320,240)
    #     encoded_str = base64.b64encode(image_byte).decode('utf-8')
        #encoded_str = base64.b64encode(image_file.read()).decode('utf-8')

    # convert to base64
    #encoded_str = base64.b64encode(stream.getvalue()).decode('utf-8')
    return encoded_str