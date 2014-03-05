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

outputFilename = 'Data/EdgeFeatures.csv'

numFeatures = 22501

#Don't forget to change the file range in the following line - (for f in files[0:1000]:)

###############################################################

###############################################################
#draws core image
def draw_core(imagePath, name): 
  path = imagePath
  image_rgb = io.imread(path)
  #resizedimg = image_rgb[187:237,187:237]
  resizedimg = image_rgb[137:287,137:287]
  image_gray = color.rgb2gray(resizedimg)
  edges = filter.canny(image_gray, high_threshold=0.1, sigma=5.5)
  scipy.misc.imsave(str("actual"+name), image_rgb)    
  scipy.misc.imsave(str("acresized"+name), resizedimg)  
  scipy.misc.imsave(str(name), edges)
  edges
  #result = hough_ellipse(edges)
  #best = result[-1]
  #a = best[3]
  #b = best[4]
  #return math.pi*2*(sqrt(a**2+b**2/2))

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
    for f in files[0:1000]:
      galName = np.array(f[:-4])
      path = inputImgs + f
	  image_rgb = io.imread(path)
	  resizedimg = image_rgb[137:287,137:287]
	  image_gray = color.rgb2gray(resizedimg)
	  edges = filter.canny(image_gray, high_threshold=0.1, sigma=5.5)
      i = np.vstack(edges)
      flat = i.flatten()
      total = np.append(galName, flat)
      writer.writerow(total)
