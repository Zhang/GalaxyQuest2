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
# Define feature extraction set

# Imgs to use - either training or test 
# specify by setting inputImgs to the appropriate directory
trainImgs = "/home/kwyn/GalaxyQuest2/images_training_rev1/"
testImgs = "/home/kwyn/GalaxyQuest2/images_test_rev1/"
inputImgs = trainImgs

# number of features extracted
numFeatures = 22501

###############################################################

###############################################################
#Gets average color
'''
def get_average_color((x,y), n, image):
 
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x+n+1):
        for t in range(y, y+n+1):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))
###############################################################
#Gets brightest pixel value
def get_brightest_pixel((x,y), n, image): 
    brightness = 0
    count = 0
    for s in range(x, x+n+1):
        for t in range(y, y+n+1):
            pixlr, pixlg, pixlb = image[s, t]
            brightPix = pixlr+pixlg+pixlb
            if brightPix > brightness:
              brightness = brightPix
            count += 1
    return brightness/3
    '''
###############################################################
#draws core image
'''
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
'''
###############################################################
#Writes features to CSV

with open('Data/EdgeFeaturesNotResizedNew.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  a = [0] * numFeatures
  writer.writerow(a)

  for root, dirs, files in os.walk(inputImgs):

    files = sorted(files)
    for f in files[0:10000]:
      galName = np.array(f[:-4])
      path = inputImgs + f
      img = io.imread(path)
      resizedimg = img[137:287,137:287]
      gimg = color.colorconv.rgb2grey(resizedimg)
#      resized = resize(resizedimg, (20,20))
      edges = filter.canny(gimg, low_threshold = 0.1, high_threshold=0.2, sigma=1.0)
#      scipy.misc.imsave(f, resized)
      i = np.vstack(edges)
      flat = i.flatten()
      total = np.append(galName, flat)
      writer.writerow(total)