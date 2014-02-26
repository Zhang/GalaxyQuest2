# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:53:44 2014

@author: kwyn
"""
import os
import csv as csv
import numpy as np
from skimage import io
from skimage.transform import resize
from sklearn.externals import joblib
from PIL import Image
import csv
from skimage import data, filter, color
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
import scipy
import math
from math import sqrt

###############################################################
trainImgs = '/Users/hackreactor1/Desktop/GalaxyQuest2/images_training_rev1/'
testImgs = '/Users/hackreactor1/Desktop/GalaxyQuest2/images_test_rev1/'
inputImgs = trainImgs

outputFilename = 'Data/AsymFeatures.csv'

numFeatures = 7

#Don't forget to change the file range in the following line - (for f in files[0:1000]:)

###############################################################

###############################################################
def get_average_brightness(array):

    count = 0
    brightness = 0
    for s in range(150):
    	brightness += array[s]
    	count+=1
    return (brightness/count)

#Working, but Y lines (450) are in different format as X lines (3x150).
def asymmetry(image):
  img = io.imread(path)
  resizedimg = img[137:287,137:287]
  gimg = color.colorconv.rgb2grey(resizedimg)
  rotated90 = np.rot90(gimg, k=1)
  imgArr1 = gimg
  imgArr2 = rotated90
  #Calculating average brightnesses of vert, horiz and one diagonal line
  originalX = get_average_brightness(imgArr1[75])
  originalY = get_average_brightness(imgArr1[0:150, 75])
  originalDiag1 = get_average_brightness(np.diagonal(imgArr1))
  
  rotated90X = get_average_brightness(imgArr2[75])
  rotated90Y = get_average_brightness(imgArr2[0:150, 75])
  rotated90Diag = get_average_brightness(np.diagonal(imgArr2))

  return originalX, originalY, originalDiag1, rotated90X, rotated90Y, rotated90Diag
  

###############################################################
#Writes features to CSV
#Path to Training pics library
#trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1/"
#Looping through the trainImgs directory
with open(outputFilename, 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  a = [0] * numFeatures
  writer.writerow(a)
  for root, dirs, files in os.walk(inputImgs):
  #sort file names into numeric order
    files = sorted(files)
    for f in files[0:10000]:
      galName = np.array(f[:-4])
      path = inputImgs + f
      asym = asymmetry(path)
      total = np.append(galName, asym)
      writer.writerow(total)
