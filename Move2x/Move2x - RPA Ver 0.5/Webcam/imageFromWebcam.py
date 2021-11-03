import glob
import os
from PIL import Image
from pathlib import Path
import shutil

def pathToFile():
    list_of_files = glob.glob(webcamFolder()) 
    latest_file = max(list_of_files, key=os.path.getctime)
    
    return latest_file

def takeImageFromWebcamFolder():
    path = pathToFile()
    print(path)
    src_dir = os.getcwd()
    dest_file = src_dir + "/temp/webcam.jpg"

    my_filePNG = Path("Temp\\webcam.png")
    if my_filePNG.is_file():
        os.remove("Temp\\webcam.png")

    shutil.move(path, dest_file)
    #shutil.copy2(path,directory)
   

    print(dest_file)
    #os.rename(dest_file, "Temp\\webcam.jpg")
    im = Image.open('Temp\\webcam.jpg')
    im.save('Temp\\align.png')
    os.remove("Temp\\webcam.jpg")    
   
def webcamFolder():
    return 'C:\\Users\\Ice_m\\Videos\\Logitech\\LogiCapture\\*.jpg'
    #return 'C:\\Users\\festo\\Videos\\Logitech\\LogiCapture\\*.jpg'

