# program to rename files

# import modules
import os
import datetime

# Define your local directory (local folder) where the files are located
directory = r"C:\Src\python"

# Get the current date and time, to later append to new file name structure

now = datetime.datetime.now()
current_date = now.strftime("%d-%m-%Y")

# Define a dictionary of old and new file names
replacement_file_names = {"one.txt": f'text_{current_date}.txt',
                          "another text.txt": f'text1_{current_date}.txt',
                          "word1.docx": f'word_{current_date}.docx',
                          "word2.docx": f'word1_{current_date}.docx',
                          "ppt.pptx": f'ppt_{current_date}.pptx',
                          }

# Loop for directory renaming
# we can use 'rename_files' as an empty list, so we can keep track of files that we've renamed
# After loop is completed we join the file rename strings together into a single string
# with line.

renamed_files = []

for filename in os.listdir(r"C:\Src\python"):
    if filename in replacement_file_names.keys():
        old_name = os.path.join(directory, filename)
        new_name = os.path.join(directory, replacement_file_names[filename])
        os.rename(old_name, new_name)
        renamed_files.append(f"{filename} -> {replacement_file_names[filename]}")

# print a message indicating files have been renamed
print("The following files have been renamed: ")
print("\n".join(renamed_files))
