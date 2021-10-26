import subprocess
import shutil
import os
from pathlib import Path
import time
def openDymo():
    path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
    path_to_file = 'resources\\Label.label'
    subprocess.call([path_to_notepad, path_to_file])

def deleteFile():
    my_filePNG = Path("resources\\Label.label")
    if my_filePNG.is_file():
        os.remove("resources\\Label.label")

def copyFile():
    # Source path
    source = "/resources/newBackUp.label"
 
    # Destination path
    destination = "/resources/Label.label"
 
    # Copy the content of
    # source to destination
 
    try:
        shutil.copyfile(source, destination)
        print("File copied successfully.")
 
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
 
    # If destination is a directory.
    except IsADirectoryError:
        print("Destination is a directory.")
 
    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
 
    # For other errors
    except:
        print("Error occurred while copying file.")

copyFile()
openDymo()
deleteFile()