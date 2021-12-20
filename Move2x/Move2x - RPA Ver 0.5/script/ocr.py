"""
This script is used for Optical character recognition 


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""


import cv2
import pytesseract as pt
from datetime import datetime
pt.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'
import re

"""
This method is used to grayed out a image, it take in as input and then returns a grayed out version of the image 

Parameters:

-image (--image): input a image

Return: 

-image (--image): output a grayed out version of the image
"""
def imageColorGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""
This method is used for Optical character recognition from a image and outputs a list of orders 

Parameters:

-image (--image): input the name of the name

Return: 

-list (--list): output a order with(the Time, the customer number, the list Product)
"""
def OCR(img):
    
    list =[] #makes a list that is empty 

    """
    Getting the file from temp folder and its type
    """
    temp = 'Temp\\'
    type = '.png'
    imgName = img
    path = temp + imgName + type 

    """
    reads the image.
    grayed out the image. 
    finds the shape of the image by the height and width of the image.
    """
    img = cv2.imread(path)
    img = imageColorGray(img)
    height, width = img.shape

    """
    Makes a empty order by,
    time, customer, list of orderProduct, product
    """
    time = ''
    customer = ''
    orderProduct = []
    product = ''

    """
    looks for images that have width bigger then 750 px
    """
    if(width >750):
        """
        Makes the image bigger so it easyer for the ocr to scan the image 
        by fx is the width and fy is the height
        """
        img = cv2.resize(img, None, fx=1.255, fy=1.3, interpolation=cv2.INTER_LINEAR)
        boxes = [] # a empty list 
        """
        try and except
        it will try to scan the image with options
        link: https://muthu.co/all-tesseract-ocr-options/
        except 
        will print out it fail to scan the image 
        """
        try:
            boxes = pt.image_to_string(img,lang='eng', config='--psm 12 --oem 1').lower() 
        except:
            print('fail  to convert')
        words = boxes.splitlines()
        """
        it will try to make a order by the word it has scan for the ocr 
        """
        for b in words:
            if len(b) > 2:
                b = b.replace('|', '')
                b = b.replace(',', '')
                b = b.replace('.', '')
                b = b.replace('pe', 'pc')
                b = b.lstrip()
                
                if(b[2] == ':' and len(b) > 10):
                    time = b[:5]
                    customer = int(re.search(r'\d+', b[5:]).group()) 
               
                try:
                    if datetime.strptime(b, '%H:%M'):
                        time = b
                        
                except:
                    lala = 2 # doesn't do anything  
                try:
                    if(int(b[1:])and len(b) > 5):
                        b = b[1:].lstrip()
                        
                    if int(b):
                        customer = int(b)
                     
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
