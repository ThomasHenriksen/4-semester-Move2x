import ImageReader as OCR
from model import order as ordersM
import cv2 
import numpy as np
import os


temp = 'Temp\\'
type = '.jpg'
path = 'last'+type 
output = os.chdir(temp)



circle = np.zeros((2,2),np.int)
counter = 0
filename = 0
out = False

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_FLAG_LBUTTON:
        circle[counter] = x,y
        counter += 1
        
img = cv2.imread(path)

while True: 
    if counter == 2:
     
     width, height = int(circle[1][0]), int(circle[1][1] - circle[0][1])
     
     pts1 = np.float32([circle[0],[circle[1][0],circle[0][1]],[circle[0][0],circle[1][1]],circle[1]])
     pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
     matrix = cv2.getPerspectiveTransform(pts1,pts2)
     imgoutput = cv2.warpPerspective(img,matrix,(width,height))
     
     if out == False:
         filename += 1
         cv2.imwrite(str(filename) +".jpg", imgoutput) 
         outPutFile = str(filename)+type

         list = OCR.OcrOrder(outPutFile)

         os.remove(outPutFile)

         ordersM = list
         for b in ordersM:
           print(b.customerNO)
         out = True
         
        

     for x in range (0,2):
         cv2.circle(img,(circle[x][0],circle[x][1],),5,(0,255,0),cv2.FILLED)

    cv2.imshow('Original Image', img)
    cv2.setMouseCallback('Original Image', mousePoints)
    cv2.waitKey(1)

#



#OCR.saveToDatabase(list)
#OCR.printOrder(list)



