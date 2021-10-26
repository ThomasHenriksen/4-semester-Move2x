import subprocess
import shutil
import os
from pathlib import Path

def openDymo():
    path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
    path_to_file = 'resources\\Label.label'
    subprocess.call([path_to_notepad, path_to_file])

def deleteFile():
    my_filePNG = Path("resources\\Label.label")
    if my_filePNG.is_file():
        os.remove("resources\\Label.label")

def copyFile():
    src = r'resources\\newBackUp.label'
    dst =  r'resources\\Label.label'
    shutil.copyfile(src, dst)

copyFile()
openDymo()
deleteFile()