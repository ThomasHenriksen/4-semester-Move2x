import cv2
import pytesseract as pt
from datetime import datetime
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
    time = ''
    customer = ''
    orderProduct = []
    product = ''
    if(width >750):
        img = cv2.resize(img, None, fx=1.255, fy=1.3, interpolation=cv2.INTER_LINEAR)
        boxes = []
        
        try:
            boxes = pt.image_to_string(img,lang='eng', config='--psm 12 --oem 1').lower() 
        except:
            print('fail  to convert')
        words = boxes.splitlines()
        
        for b in words:
            if len(b) > 2:
                b = b.replace('|', '')
                b = b.lstrip()
                print(b)
                if(b[2] == ':' and len(b) > 10):
                    time = b[:5]
                    customer = b[5:].lstrip()
               
                try:
                    if datetime.strptime(b, '%H:%M'):
                        time = b
                        
                except:
                    lala = 2
                try:
                    if(int(b[1:])and len(b) > 5):
                        b = b[1:].lstrip()
                        print('here')
                        print(b )
                    if int(b):
                        customer = b
                     
                except:
                    lala = 2
                try:
                    
                    if len(b) > 20:
                        product = b
                        orderProduct.append(product)
                        
                        
                except:
                    lala = 2
                
   
    if time:
        if customer:
            if orderProduct:
                list.append(time)
                list.append(customer)
                list.append(orderProduct)
    
    return list
