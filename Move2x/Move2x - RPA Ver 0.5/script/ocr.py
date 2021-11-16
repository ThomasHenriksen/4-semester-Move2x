import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'



def imageColorGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def listOfWords(img):
    
    list =[]
    
    temp = 'Temp\\'
    type = '.png'
    imgName = img
    path = temp + imgName + type 
    
    img = cv2.imread(path)
    img = imageColorGray(img)
    height, width = img.shape
    
    if(width >600):
        img = cv2.resize(img, None, fx=1.255, fy=1.3, interpolation=cv2.INTER_LINEAR)
        boxes = []
        try:
            boxes = pt.image_to_string(img,lang='eng', config='--psm 12 --oem 1').lower() 
        except:
            print('fail  to convert')
        words = boxes.splitlines()
        for b in words:
            
            list.append(b)
    
    

    
    return list
