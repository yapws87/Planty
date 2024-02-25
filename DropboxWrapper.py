import dropbox 
import os
import requests

drop_key = os.getenv('DROPBOX_KEY')
drop_secret = os.getenv('DROPBOX_SECRET')
drop_access = os.getenv('DROPBOX_ACCESS')
drop_refresh = os.getenv('DROPBOX_REFRESH')

#
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
        #self.dbx = dropbox.Dropbox(drop_access)
        #self.dropbox_folder = 'Planty'

    def __init__(self,drop_key,drop_secret,drop_access):
        print(f"drop_key : {drop_key}")
        print(f"drop_secret : {drop_secret}")
        print(f"drop_access : {drop_access}")
        #self.dbx = dropbox.Dropbox(drop_access)
        #self.dropbox_folder = 'Planty'
    def upload_file(self,file_path,dropbox_path):
        #file_path = '/pi/github/Planty/image.jpg'  # Path to your image file on Raspberry Pi
        #dropbox_path = '/Planty/image.jpg'  # Path where you want to store the image in Dropbox
        drop_access = get_access_token()
        self.dbx =dropbox.Dropbox(drop_access)
        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), dropbox_path)


def get_access_token():
    token_endpoint = "https://api.dropbox.com/oauth2/token"
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': drop_refresh,
        'client_id': drop_key,
        'client_secret': drop_secret,
    }

    response = requests.post(token_endpoint, data=data)
    tokens = response.json()
    #print("Access Token:", tokens['access_token'])
    return tokens['access_token']

def get_token(app_key, app_secret):

    # Your app's credentials
    APP_KEY = app_key
    APP_SECRET = app_secret
    REDIRECT_URI = 'http://localhost:5000/callback'
    
    # Step 1: Direct users to authorize your app
    authorization_url = f"https://www.dropbox.com/oauth2/authorize?response_type=code&client_id={APP_KEY}&token_access_type=offline&redirect_uri={REDIRECT_URI}"
    print(authorization_url)
    
    # Step 2: After user authorization, receive the authorization code at your redirect URI
    authorization_code = input("Enter the authorization code: ")
    

    # Step 3: Exchange authorization code for access token and refresh token
    token_endpoint = "https://api.dropbox.com/oauth2/token"
    data = {
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'client_id': APP_KEY,
        'client_secret': APP_SECRET,
        'redirect_uri': REDIRECT_URI,

    }

    response = requests.post(token_endpoint, data=data)
    tokens = response.json()

    print(tokens)
    print("Access Token:", tokens['access_token'])
    


if __name__=="__main__":
    
    import sys

    drop_key = sys.argv[1]
    drop_secret = sys.argv[2]
    drop_access = sys.argv[3]
    drop_refresh = sys.argv[4]
    get_token(drop_key, drop_secret, drop_refresh)
    
    # dbox = Dropboxy(drop_key,drop_secret,drop_access)
    # image_path = r"C:\Users\yapws87\Downloads\original.jpg"
    # import dgozf6-D_4WwAAAAAAAA0ouEH8MH0b-iYZEvO5gsB48Matetime
    # now = datetime.datetime.now()
    # filename = '/' + str(now) + '.jpg'
    # dbox.upload_file(image_path,'/test.jpg')