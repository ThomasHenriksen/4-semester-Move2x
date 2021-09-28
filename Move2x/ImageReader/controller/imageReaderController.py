import cv2
import pytesseract as pt
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
list = []
def imageColorRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def listOfWords(path):
    img = cv2.imread(path)
    img = imageColorRGB(img)
    hImg, wImag, channels  = img.shape
    boxes = pt.image_to_data(img) 
    
    for x,b in enumerate(boxes.splitlines()):
         if x!=0: 
            b = b.split()
            if len(b) == 12:
               x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
               list.append(b[11])
    return list
               
 