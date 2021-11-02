import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'


def imageColorRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def imageColorGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def listOfWords():
    list =[]
    temp = 'Temp\\'
    type = '.png'
    imgName = 'webcam'
    path = temp + imgName + type 
    img = cv2.imread(path)
    img = imageColorGray(img)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    

    
    boxes = pt.image_to_string(img,lang='eng', config='--psm 12 --oem 1').lower() 
    


    test = boxes.splitlines()
    for b in test:
        list.append(b)
    
    
    
    return list
