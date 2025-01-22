# Auto Upload IG via Meta API

This Python script automates the process of uploading videos from a specified directory to Instagram Reels using the Meta API. It's designed for content creators participating in Meta's Breakthrough Bonus program or anyone looking to streamline their content upload process.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)

## Setup

### 1. Environment Setup

- **Create a `.env` file**: In your project directory, create a file named `.env` in a subdirectory called `env`. This file will store your sensitive API information.

- **Add Environment Variables**: Inside `env\.env`, add the following variables with your Meta API credentials:

```plaintext
API_VERSION=your_api_version
INSTAGRAM_ACCOUNT_ID=your_instagram_account_id
ACCESS_TOKEN_META=your_access_token
directory=path_to_your_video_directory
```

Replace `your_api_version`, `your_instagram_account_id`, `your_access_token`, and `path_to_your_video_directory` with your actual values. The directory should be the full path to the folder containing your video files.

### 2. Directory Structure
Your project directory should look like this:

```Structure
project_root/
│
├── env/
│   └── .env
│
├── your_video_directory/
│   ├── video1.mp4
│   ├── video1.txt
│   └── video2.mp4
│
└── auto_upload_ig.py
```

- Video Files: Place your .mp4 video files in your_video_directory.
- Caption Files: Optionally, for each video, you can place a .txt file with the same name (but different extension) in the same directory. The content of this file will be used as the caption for the video. If no .txt file is found, a default caption will be used.
