import dropbox 
import os

drop_key = os.getenv('DROPBOX_KEY')
drop_secret = os.getenv('DROPBOX_SECRET')
drop_access = os.getenv('DROPBOX_ACCESS')
#eplace 'your_access_token' with the token you generated

def load_access_token(file_path):
    """Load the Dropbox access token from a file."""
    try:
        with open(file_path, 'r') as file:
            access_token = file.read().strip()  # Remove any possible whitespace
        return access_token
    except FileNotFoundError:
        print("Access token file not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

class Dropboxy:
    def __init__(self,):
        print(f"drop_key : {drop_key}")
        print(f"drop_secret : {drop_secret}")
        print(f"drop_access : {drop_access}")
        self.dbx = dropbox.Dropbox(drop_access)
        #self.dropbox_folder = 'Planty'
    def upload_file(self,file_path,dropbox_path):
        #file_path = '/pi/github/Planty/image.jpg'  # Path to your image file on Raspberry Pi
        #dropbox_path = '/Planty/image.jpg'  # Path where you want to store the image in Dropbox

        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), dropbox_path)

if __name__=="__main__":
    dbox = Dropboxy()
    
    image_path = "/home/pi/github/Planty/image.jpg"
    #import datetime
    #now = datetime.datetime.now()
    #filename = '/' + str(now) + '.png'
    dbox.upload_file(image_path,'/test.jpg')