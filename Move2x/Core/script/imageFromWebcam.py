import glob
import os
from PIL import Image
from pathlib import Path
import shutil

def pathToFile():
    list_of_files = glob.glob('C:\\Users\\Ice_m\\Videos\\Logitech\\LogiCapture\\*') 
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def takeImageFromWebcamFolder():
    path = pathToFile()
    print(path)
   
    my_filePNG = Path("Temp\\webcam.png")
    if my_filePNG.is_file():
        os.remove("Temp\\webcam.png")
    shutil.copy2(path,"Temp\\webcam.jpg")
     
    #os.rename(latest_file, "Temp\\webcam.jpg")
    im = Image.open('Temp\\webcam.jpg')
    im.save('Temp\\webcam.png')
    os.remove("Temp\\webcam.jpg")    
   

    list_of_files = glob.glob('Temp\\*') 
    latest_file = max(list_of_files, key=os.path.getctime)

takeImageFromWebcamFolder()
