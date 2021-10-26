import subprocess
import shutil
import os

def openDymo():
    my_file = Path("resources\\Label.label")
    if my_file.is_file():
        os.remove("resources\\Label.label")


    src = r'resources\\newBackUp.label'
    dst =  r'resources\\Label.label'
    shutil.copyfile(src, dst)


    path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
    path_to_file = 'resources\\Label.label'

    subprocess.call([path_to_notepad, path_to_file])

openDymo()