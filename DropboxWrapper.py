import dropbox 
import os

drop_key = os.getenv('DROPBOX_KEY')
drop_secret = os.getenv('DROPBOX_SECRET')
drop_access = os.getenv('DROPBOX_ACCESS')

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
        self.dbx = dropbox.Dropbox(drop_access)
        #self.dropbox_folder = 'Planty'
    def upload_file(self,file_path,dropbox_path):
        #file_path = '/pi/github/Planty/image.jpg'  # Path to your image file on Raspberry Pi
        #dropbox_path = '/Planty/image.jpg'  # Path where you want to store the image in Dropbox

        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), dropbox_path)


def get_token():
    import requests

    # Your app's credentials
    APP_KEY = ''
    APP_SECRET = ''
    REDIRECT_URI = 'http://localhost:5000/callback'
    
    # Step 1: Direct users to authorize your app
    authorization_url = f"https://www.dropbox.com/oauth2/authorize?response_type=code&client_id={APP_KEY}&redirect_uri={REDIRECT_URI}"
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
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(token_endpoint, data=data)
    tokens = response.json()

    # Initialize Dropbox OAuth2 flow
    # auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

    # access_token, refresh_token = auth_flow.finish(authorization_code)
    # print("Access Token:", access_token)
    # print("Refresh Token:", refresh_token)
    print(tokens)
    print("Access Token:", tokens['access_token'])
    print("Refresh Token:", tokens['refresh_token'])

if __name__=="__main__":
    #get_token()
    
    dbox = Dropboxy()
    image_path = r"C:\Users\yapws87\Downloads\original.jpg"
    import datetime
    now = datetime.datetime.now()
    filename = '/' + str(now) + '.jpg'
    dbox.upload_file(image_path,'/test.jpg')