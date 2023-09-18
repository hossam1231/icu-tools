import subprocess
from datetime import datetime

time_stamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
file_path = f"movies/{time_stamp}.mov"

# Run screen recording in the background and save it in the "movies" folder
subprocess.Popen(["screencapture", "-v", file_path])

# Run the server in the background
subprocess.Popen(["yarn", "dev"])

# Wait for a key press to stop the processes
input("Press any key to stop...")

# Terminate the screen recording process
subprocess.Popen.terminate()

# Terminate the server process
subprocess.Popen.terminate()

# import subprocess
# from datetime import datetime
# import time
# import random
# import os

# def commit_random():
#     # Add code to commit a random commit on GitHub
#     # You can use GitPython library or GitHub API to achieve this

# def play_youtube_video():
#     # Add code to play a YouTube video
#     # You can use a library like pytube or webbrowser to achieve this

# def record_screen_and_execute():
#     time_stamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
#     file_path = f"movies/{time_stamp}.mov"

#     # Run screen recording in the background and save it in the "movies" folder
#     subprocess.Popen(["screencapture", "-v", file_path])

#     # Run the server in the background
#     subprocess.Popen(["next", "dev"])

#     # Start a loop to commit and play video every ten seconds
#     while True:
#         commit_random()
#         play_youtube_video()
#         time.sleep(10)

#         # Terminate the screen recording process after 10 seconds
#         subprocess.Popen.terminate()

#         # Check if the screen recording process is still running
#         if subprocess.Popen.poll() is not None:
#             # If the process has terminated, break the loop
#             break

#     # Terminate the server process
#     subprocess.Popen.terminate()

#     # Wait for a key press to stop the processes
#     input("Press any key to stop...")

#     # Delete the recorded file
#     os.remove(file_path)