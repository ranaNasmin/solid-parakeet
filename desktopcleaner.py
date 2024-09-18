# This is a python script to build a download cleaner
# This helps to categorise and clean the download folder of your pc
# First import the os module to perform file actions
# Import the datetime module to get the date and time the files were created
import time
import shutil
import pathlib
import os

# First define the source directory (In this case it is downloads folder)
src_folder = pathlib.Path(r"C:\Users\hp\Desktop\new-folder")

if os.access(src_folder, os.R_OK):
    print(f"The file {src_folder} is readable.")
else:
    print(f"The file {src_folder} is not readable.")

# Check if the file is writable
if os.access(src_folder, os.W_OK):
    print(f"The file {src_folder} is writable.")
else:
    print(f"The file {src_folder} is not writable.")

# Accepting extensions of images:
image_extension = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                   ".raw",
                   ".arw", ".cr2", ".nrw",
                   ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf",
                   ".jpx",
                   ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

# Accepting extensions of videos:
vdo_extension = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                 ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

# Accepting extensions of audios:
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

# Accepting extensions of documents:
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# Building the system for file organization.
# Create different folders for different type of files like (images, audios, videos, and documents).

folders = {"images": pathlib.Path(src_folder / 'images'),
           "videos": pathlib.Path(src_folder / 'videos'),
           "audios": pathlib.Path(src_folder / 'audios'),
           "documents": pathlib.Path(src_folder / 'documents'),
           "unknown": pathlib.Path(src_folder / 'Unknown')}


# write a function to check if the file exist and move accordingly
def move_file(file, destination_folder):
    # assign the destination variable to check if the file already exists
    file_destination = destination_folder / file.name
    if file_destination.exists():
        # if it already exists ask the user if they want to overwrite it or skip it
        overwrite_consent = input(f"This file {file.name} already exits do you want to overwrite it? (Y/N)").lower()
        # overwrite the file if 'y'
        if overwrite_consent == 'y':
            print(f"Overwriting the file....")
            new_name = f"{file.stem}_{int(time.time())}{file.suffix}"
            file_destination = destination_folder / new_name
            file.replace(file_destination)
            print(f"Successfully moved your file to new destination {file_destination} ")
        # skip the file if 'n'
        elif overwrite_consent == 'n':
            print(f"File {file.name} already exists in the destination folder. Skipping.")
        # skip the file if invalid input
        else:
            print(f"invalid input skipping the file {file.name}: ")
    # replace the file directly if such a file doesn't' exist
    else:
        shutil.move(str(file), str(file_destination))

# Function to handle file processing. If the file-extension is found in any extension list, then the move_file() is
# called and arguments file and folder_destination is passed
def file_extension(file):
    if file.suffix.lower() in image_extension:
        print("its an image extension")
        move_file(file, folders["images"])
    elif file.suffix.lower() in vdo_extension:
        move_file(file, folders["videos"])
    elif file.suffix.lower() in audio_extensions:
        move_file(file, folders["audios"])
    elif file.suffix.lower() in document_extensions:
        move_file(file, folders["documents"])
    else:
        move_file(file, folders["unknown"])


# Now accessing files real time
# First get the current files in the directory
def get_current_files():
    return set(file for file in src_folder.iterdir() if file.is_file())


# function to monitor directory for changes
def monitor_folder(interval=10):
    print("Monitor folder for new files: ")
    # Access new files from the get_current_files()
    known_files = get_current_files()
    try:
        while True:
            time.sleep(interval)
            for new_file in known_files:
                print(f"{new_file} is a new_file found")
                if new_file.is_file():
                    for file in known_files:
                        print(f"New new_file detected {file.name}: ")
                        file_extension(file)
    except FileNotFoundError as e:
        print("file not found")


monitor_folder(interval=5)
