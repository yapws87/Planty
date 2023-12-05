import dropbox 
import os

drop_key = os.getenv('DROPBOX_KEY')
drop_secret = os.getenv('DROPBOX_SECRET')
drop_access = os.getenv('DROPBOX_ACCESS')
#eplace 'your_access_token' with the token you generated



class Dropboxy:
    def __init__(self,):
        self.dbx = dropbox.Dropbox(drop_access)
        #self.dropbox_folder = 'Planty'
    def upload_file(self,file_path,dropbox_path):
        #file_path = '/pi/github/Planty/image.jpg'  # Path to your image file on Raspberry Pi
        #dropbox_path = '/Planty/image.jpg'  # Path where you want to store the image in Dropbox

        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), dropbox_path)