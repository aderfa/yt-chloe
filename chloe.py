from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request  # Import this module
from datetime import datetime
import pytz
import os
import pickle

# Ganti dengan path ke file kredensial OAuth 2.0 Anda
CLIENT_SECRETS_FILE = 'test.json'
TOKEN_PICKLE_FILE = 'token.pickle'
# Ganti 'VIDEO_ID' dengan ID video yang ingin Anda ubah judulnya
VIDEO_ID = 'YGzH8dgRjl8'

# Tanggal mulai
START_DATE = datetime(2023, 5, 14, tzinfo=pytz.timezone('Asia/Jakarta'))

# OAuth 2.0 Scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    credentials = None
    # Cek apakah token sudah ada
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            credentials = pickle.load(token)
    # Jika tidak ada token atau token sudah expired, lakukan otorisasi
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Simpan token ke file
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(credentials, token)
    return build('youtube', 'v3', credentials=credentials)

def get_days_since_start():
    now = datetime.now(pytz.timezone('Asia/Jakarta'))
    delta = now - START_DATE
    return delta.days

def change_video_title(youtube, video_id, new_title):
    try:
        # Ambil detail video
        video_response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        # Ubah judul video
        video_snippet = video_response['items'][0]['snippet']
        video_snippet['title'] = new_title

        # Update video
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
    
    # Hitung jumlah hari
    days_since_start = get_days_since_start()
    new_title = f"Menunggu Chloe Stream Day {days_since_start}"
    
    # Ubah judul video
    change_video_title(youtube, VIDEO_ID, new_title)
