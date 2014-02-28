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
from skimage import img_as_bool
from skimage.morphology import dilation, disk, skeletonize

###############################################################
trainImgs = '/home/kwyn/GalaxyQuest2/images_training_rev1/'
testImgs = '/home/kwyn/GalaxyQuest2/images_test_rev1/'
inputImgs = trainImgs

outputFilename = '/home/kwyn/GalaxyQuest2/Data/TRAINSkeletonFeatures.csv'

numFeatures = 401

#Don't forget to change the file range in the following line - (for f in files[0:1000]:)

###############################################################

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
      img = io.imread(path, as_grey=True)
      cropped = img[137:287,137:287]
      resized = resize(cropped, (20,20))
      im = ~img_as_bool(resized)
#      selem = disk(6) 
#      d = dilation(resized, selem)
      sk = skeletonize(im)
      i = np.vstack(sk)
      flat = i.flatten()
      total = np.append(galName, flat)
      writer.writerow(total)
