"""
This script is used for align the image so its easyer for the ocr to scan the image 


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""

from __future__ import print_function
import cv2
import numpy as np
import os
from script import SearchBot

"""
This method is used for to align the image from the temp folder, where the name is align. it will save the new image as webcam.png in the temp folder 

"""
def alignImages():
  """
  how good the the align have to be 
  """
  MAX_FEATURES = 1000
  GOOD_MATCH_PERCENT = 1

  tempSearch = 'temp\\'
  typeSearch = '.png'
  nameSearch = 'align'  

  imFilename = tempSearch + nameSearch + typeSearch 
  
  im1 = cv2.imread(imFilename, cv2.IMREAD_COLOR)

  refFilename = "resources\\ref.png"
  
  im2 = cv2.imread(refFilename, cv2.IMREAD_COLOR)

  # Convert images to grayscale
  im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
  im1Gray = cv2.resize(im1Gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
  im2Gray = cv2.resize(im2Gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

  # Detect ORB features and compute descriptors.
  orb = cv2.ORB_create(MAX_FEATURES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
  
  # Sort matches by score
  #matches.sort(key=lambda x: x.distance, reverse=False)

  # Remove not so good matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]

  # Draw top matches
  imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
  

  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

  # Use homography
  height, width, channels = im2.shape
  im1Reg = cv2.warpPerspective(im1, h, (width, height))
  outFilename = tempSearch+"webcam.png" 
  
  #os.remove(outFilename)
 
  cv2.imwrite(outFilename, im1Reg) #saves the file as webcam.png in the temp folder 


  """
  Checks if the align image look like the order card if not it will do the method again 

  """
  if(SearchBot.check('webcam','ref') < 0.64):
      alignImages()
 
  
