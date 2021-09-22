import cv2
import pytesseract as pt
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('C:\\Users\\Ice_m\\2 semester\\4-semester-Move2x\\Move2x\\ImageReader\\ocr-sample2.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pt.image_to_string(img))


hImg, wImag, channels  = img.shape
boxes = pt.image_to_data(img) 
list = []
for x,b in enumerate(boxes.splitlines()):
     if x!=0: 
        b = b.split()
        print(b)

        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img, (x,y),(w+x,h+y),(0,0,255),1)
            

print(list)
cv2.imshow('Result', img)
cv2.waitKey(0)
