from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request 
from datetime import datetime
import pytz
import os
import pickle

# File OAuth 2.0
CLIENT_SECRETS_FILE = 'test.json'
TOKEN_PICKLE_FILE = 'token.pickle'

VIDEO_ID = 'YGzH8dgRjl8'

# Tanggal mulai stream chloe
START_DATE = datetime(2023, 5, 14, tzinfo=pytz.timezone('Asia/Jakarta'))


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    credentials = None
    
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            credentials = pickle.load(token)
   
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(credentials, token)
    return build('youtube', 'v3', credentials=credentials)

def get_days_since_start():
    now = datetime.now(pytz.timezone('Asia/Jakarta'))
    delta = now - START_DATE
    return delta.days

def change_video_title(youtube, video_id, new_title):
    try:
        
        video_response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        
        video_snippet = video_response['items'][0]['snippet']
        video_snippet['title'] = new_title

        
        update_response = youtube.videos().update(
            part='snippet',
            body={
                'id': video_id,
                'snippet': video_snippet
            }
        ).execute()

        print(f"Judul video berhasil diubah menjadi: {new_title}")
        print(update_response)

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")

if __name__ == '__main__':
    youtube = get_authenticated_service()
    
    
    days_since_start = get_days_since_start()
    new_title = f"Menunggu Chloe Stream Day {days_since_start}"
    
    
    change_video_title(youtube, VIDEO_ID, new_title)
