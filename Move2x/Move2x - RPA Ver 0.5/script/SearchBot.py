import numpy as np
import cv2 as cv
import pyautogui as pg
import pyautogui, time
from PIL import Image as imgTesting
             

def find_label(take_screenshot, Label): 
    tempSearch = 'resources\\'
    typeSearch = '.png'
    nameSearch = Label
    pathSearch = tempSearch + nameSearch + typeSearch 
    temp = 'temp\\'
    type = '.png'
    path = temp + take_screenshot + type 
    haystack_img = cv.imread(path) #Screenshot
    #haystack_img = cv.resize(haystack_img, (1024, 720))
    needle_img = cv.imread(pathSearch)#Label img to find with in screenshot
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED) # match Screenshot and Label img 

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    #print('Best match top left positopn: %s' % str(max_loc))
    print('Best match confidence: %s' % str(max_val))
    # Sets the level off accepteable match with in screenshot
    threshold = 0.70
    if(max_val >= threshold):
        #print(Label + ' is foundt')

    #get dimensions of the needle image
        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        return max_loc

def searchForAutoCrop(): 
    topCornerResour = 'resources\\'
    topCornerType = '.png'
    topCornerSearch = 'topCorner'
    topCornerpath = topCornerResour + topCornerSearch + topCornerType 
    bottomCornerResourSearch = 'resources\\'
    bottomCornerTypeSearch = '.png'
    bottomCornerNameSearch = 'bottomCorner'
    bottomCornerPathSearch = bottomCornerResourSearch + bottomCornerNameSearch + bottomCornerTypeSearch 
    temp = 'temp\\'
    type = '.png'
    path = temp + 'align' + type 

    method = cv.TM_CCOEFF_NORMED

    img = cv.imread(path) #Screenshot
    height, width, __ = img.shape
    #haystack_img = cv.resize(haystack_img, (1024, 720))
    topCorner_img = cv.imread(topCornerpath)#Label img to find with in screenshot
    bottomCorner_img = cv.imread(bottomCornerPathSearch)#Label img to find with in screenshot
    topCornerResult = cv.matchTemplate(img, topCorner_img, method) # match Screenshot and Label img 
    bottomCornerResult = cv.matchTemplate(img, bottomCorner_img, method) # match Screenshot and Label img 
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(topCornerResult)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(bottomCornerResult)
    #print('Best match top left positopn: %s' % str(max_loc))
    #print('Best match confidence: %s' % str(max_val))
    # Sets the level off accepteable match with in screenshot
    bottomCorner_w = bottomCorner_img.shape[1]
    bottomCorner_h = bottomCorner_img.shape[0]

    threshold = 0.95
    yloc, xloc = np.where( topCornerResult >= threshold)
    yloc2, xloc2 = np.where( bottomCornerResult >= threshold)
    findCropCoordinates  = []
    for(x,y) in zip(xloc, yloc):
        
        fundet = False
        Coordinates = []
        for(x2,y2) in zip(xloc2, yloc2):
            if(x < x2 and y < y2 and fundet == False):
                if(x2 > 1250):
                    if(x < 400):
                        
                        fundet = True
                        Coordinates.append(x)
                        Coordinates.append(y)
                        Coordinates.append(x2)
                        Coordinates.append(y2)
                        findCropCoordinates.append(Coordinates)
    #index = 0 

    #while(index < len(findCropCoordinates)-1):
        
        #if((findCropCoordinates[index+1][1]-findCropCoordinates[index][1])> 5):
        #    findCropCoordinates.remove(findCropCoordinates[index])
        #index+=1


    listOfFiles = []
    i = 0
    for(x,y,x2,y2) in findCropCoordinates:
        
        imgCrop = imgTesting.open(path)
        img2 = imgCrop.crop((x,y,  (x2),(y2+5)  ))
        fileName = "img"+str(i)
        img2.save(temp+fileName+type)
        listOfFiles.append(fileName)
        i+=1
    
    return listOfFiles

   
        
def check(take_screenshot, whatToCheck): 
    tempSearch = 'resources\\'
    typeSearch = '.png'
    nameSearch = whatToCheck
    #print(nameSearch)
    pathSearch = tempSearch + nameSearch + typeSearch 
    temp = 'temp\\'
    type = '.png'
    path = temp + take_screenshot + type 
    haystack_img = cv.imread(path) #Screenshot
  
    needle_img = cv.imread(pathSearch)#Label img to find with in screenshot
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED) # match Screenshot and Label img 

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
   # print('Best match confidence: %s' % str(max_val))


    return max_val
