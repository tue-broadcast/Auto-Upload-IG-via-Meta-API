import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from the .env file with the corrected path
result = load_dotenv(dotenv_path='env\.env')
print(f".env file loaded: {result}")

# API Configuration
API_VERSION = os.getenv('API_VERSION')
INSTAGRAM_ACCOUNT_ID = os.getenv('INSTAGRAM_ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN_META')

# Log file to keep track of uploaded videos
VIDEO_DIR = os.getenv('directory')
LOG_FILE = os.path.join(VIDEO_DIR, 'uploaded_videos_IG.log')

def upload_reel(video_path, caption):
    try:
        # Step 1: Initialize an Upload Session for Reels
        init_url = f"https://graph.facebook.com/{API_VERSION}/{INSTAGRAM_ACCOUNT_ID}/media"
        init_params = {
            'media_type': 'REELS',
            'upload_type': 'resumable',
            'caption': caption,
            'access_token': ACCESS_TOKEN
        }
        init_response = requests.post(init_url, data=init_params)
        if init_response.status_code != 200:
            raise Exception(f"Failed to initialize upload session: {init_response.text}")

        container_id = init_response.json()['id']
        upload_url = init_response.json()['uri']

        # Step 2: Upload the Video using Resumable Upload Protocol
        file_size = os.path.getsize(video_path)
        headers = {
            'Authorization': f'OAuth {ACCESS_TOKEN}',
            'offset': '0',
            'file_size': str(file_size)
        }

        with open(video_path, 'rb') as video_file:
            upload_response = requests.post(upload_url, headers=headers, data=video_file)
        
        if upload_response.status_code != 200 or not upload_response.json()['success']:
            raise Exception(f"Video upload failed: {upload_response.text}")

        # Step 3: Publish the reel
        publish_url = f"https://graph.facebook.com/{API_VERSION}/{INSTAGRAM_ACCOUNT_ID}/media_publish"
        publish_params = {
            'creation_id': container_id,
            'access_token': ACCESS_TOKEN
        }
        publish_response = requests.post(publish_url, params=publish_params)

        if publish_response.status_code != 200:
            raise Exception(f"Failed to publish reel: {publish_response.text}")

        print(f"Reel published successfully. Media ID: {publish_response.json()['id']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def log_uploaded_video(video_path):
    video_name = os.path.basename(video_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Uploaded: {video_name}\n"
    
    with open(LOG_FILE, 'a', encoding='utf-8') as log:
        log.write(log_entry)

def check_for_duplicate(video_path):
    video_name = os.path.basename(video_path)
    if not os.path.exists(LOG_FILE):
        return False
    
    with open(LOG_FILE, 'r', encoding='utf-8') as log:
        for line in log:
            if video_name in line:
                return True
    return False

def get_caption(video_name, folder_path):
    # Construct the expected path for the .txt file
    txt_path = os.path.join(folder_path, os.path.splitext(video_name)[0] + ".txt")
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    return f"Auto-uploaded: {video_name}"  # Default caption if no .txt file found

def auto_upload_reels(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp4'):
            video_path = os.path.join(folder_path, filename)
            if not check_for_duplicate(filename):
                # Get the caption from the corresponding .txt file if it exists
                caption = get_caption(filename, folder_path)
                upload_reel(video_path, caption)
                log_uploaded_video(filename)
                return
            else:
                print(f"Skipping {filename} - already uploaded")
    return

if __name__ == "__main__":
    if VIDEO_DIR and os.path.exists(VIDEO_DIR):
        auto_upload_reels(VIDEO_DIR)
    else:
        print("Error: Video directory not set or does not exist.")