<a href="buymeacoffee.com/tue_broadcast" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>

# Auto Upload IG via Meta API

This Python script automates the process of uploading videos from a specified directory to Instagram Reels using the Meta API. It's designed for content creators participating in Meta's Breakthrough Bonus program or anyone looking to streamline their content upload process.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher OR https://www.anaconda.com/download (easy for install python in WIN11)
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

### 3. Running the Script

- Open Terminal/Command Prompt: Navigate to your project directory.
- Run the Script: Execute the script with:

```bash
python auto_upload_ig.py
```

The script will:
- Check for new videos in the specified directory.
- Upload each new `.mp4` video to Instagram Reels.
- Use the corresponding `.txt` file for captions if available, or provide a default caption.
- Log each upload in `uploaded_videos_IG.log` to avoid duplicates.



## Setting Up Task Scheduler in Windows 11

To automate the execution of this script on Windows 11 with Conda Python, follow these steps:

1. **Open Task Scheduler**: 
   - Click on the Windows icon or press `Win` key, type "Task Scheduler", and select it from the results.

2. **Create Basic Task**:
   - In the Task Scheduler, right-click on "Task Scheduler Library" and select "Create Basic Task...".

3. **General Tab**:
   - Give your task a name like "Auto Upload IG".
   - Check "Run whether user is logged on or not" if you want the task to run even when you're not logged in.
   - Check "Run with highest privileges" to ensure the task has the necessary permissions.

4. **Triggers Tab**:
   - Click "New..." to add a trigger.
   - Choose "Daily" if you want it to run every day, or select another option based on your needs.
   - Set the start time and optionally the end date if needed.

5. **Actions Tab**:
   - Click "New..." to add an action.
   - Select "Start a program" as the action type.
   - In the "Program/script" field, browse to and select the `conda.exe` from your Anaconda or Miniconda installation directory (typically `C:\Users\YourUsername\anaconda3\condabin\conda.bat` or similar).
   - In the "Add arguments (optional)" field, type the following:
     ```
     run python auto_upload_ig.py --name your_env_name
     ```
     Replace `your_env_name` with the name of your Conda environment where your script dependencies are installed.
   - In the "Start in (optional)" field, enter the path to your project root directory to ensure the script can find the `.env` file.
  
   OR

   - Click "New..." to add an action.
   - Select "Start a program" as the action type.
   - In the "Program/script" field, browse to and select `python.exe` from your Python installation directory (typically `C:\PythonXX\python.exe`, where XX is your Python version).
   - In the "Add arguments (optional)" field, type `auto_upload_ig.py`.
   - In the "Start in (optional)" field, enter the path to your project root directory to ensure the script can find the `.env` file.

6. **Conditions & Settings**:
   - Adjust conditions like "Start the task only if the computer is idle for" if necessary.
   - In the Settings tab, you might want to check options like "Run task as soon as possible after a scheduled start is missed" for reliability.

7. **Finish**:
   - Click "OK" to save your task. You might need to enter your administrator credentials to save the task.

Now your task is set to run automatically according to the schedule you've set. Remember, you can always go back and edit this task if you need to change the schedule or other settings.
## 
This README provides all the necessary information for a new user to get started with your project. Remember to create a LICENSE.md file with the MIT License text if you decide to use it. Also, ensure you keep your .env file out of version control by adding env/.env to your .gitignore file.

<a href="buymeacoffee.com/tue_broadcast" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>
