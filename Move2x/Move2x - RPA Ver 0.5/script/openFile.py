import subprocess
import shutil
import os
from pathlib import Path
import time
from threading import Thread
def openFile():
    path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
    path_to_file = 'resources\\Label.label'
    subprocess.Popen([path_to_notepad, path_to_file])
    

def deleteFile():
    my_filePNG = Path("resources\\Label.label")
    if my_filePNG.is_file():
        os.remove("resources\\Label.label")

def copyFile():
    # Source path
    source = "resources\\newBackUp.label"
 
    # Destination path
    destination = "resources\\Label.label"
 
    # Copy the content of
    # source to destination
    shutil.copyfile(source, destination)
  

