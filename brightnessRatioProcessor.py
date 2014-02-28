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
trainImgs = '/home/kwyn/GalaxyQuest2/images_training_rev1/'
testImgs = '/home/kwyn/GalaxyQuest2/images_test_rev1/'
inputImgs = trainImgs

outputFilename = '/home/kwyn/GalaxyQuest2/Data/TRAINbrightnessRatioFeatures.csv'

numFeatures = 2

#Don't forget to change the file range in line 85 (for f in files[0:1000]:)

###############################################################

##############################################################
#Finds total brightness of entire image
#x and y are starting pixel coordinates of image
#n is distance from starting point to endpoint
def totalBrightness((x,y), n, image):
    brightness = 0

    for s in range(x, x+n):
        for t in range(y, y+n):
            pixlr, pixlg, pixlb = image.getpixel((s,t))
            brightness += pixlr+pixlg+pixlb
    brightnessTotal = brightness/3
    return brightnessTotal

##############################################################
#Finds ratio of area containing 75% of image's total brightness to area containing 25% of total brightness    
def brightnessRatios(image):
    img = Image.open(image).convert('RGB')
    resizedimg = img.crop((138,138,288,288)) 
    brightnessTotal = totalBrightness((0,0), 150, resizedimg)
    sections = []
#    distance25 = 0
    for i in range(1,75):
        section25 = resizedimg.crop((75-i, 75-i, 75+i, 75+i))
        if totalBrightness((0,0),2*i,section25) >= brightnessTotal * 0.25:
            sections.append(i+1)
            distance25 = i
            break
    for i in range(distance25, 75):
        section75 = resizedimg.crop((75-i, 75-i, 75+i, 75+i)) 
        if totalBrightness((0,0),2*i,section75) >= brightnessTotal * 0.75:
            sections.append(i+1)
            break
        if i == 74:
            sections.append(i+1)
    brightnessRatio = sections[1]/float(sections[0])
    return brightnessRatio

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
    for f in files:
      galName = np.array(f[:-4])
      path = inputImgs + f
      br = brightnessRatios(path)
      total = np.append(galName, br)
      writer.writerow(total)
