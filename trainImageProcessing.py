# -*- coding: utf-8 -*-
"""
Image file feature extraction
Created on Fri Feb 14 11:45:56 2014

@author: kwyn
"""
import os
import csv as csv
import numpy as np
from skimage import io
from skimage import color
from skimage.transform import resize

#Training pics library
trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1"
#create a csv writer for trainFeatures
trainFeatures = csv.writer(open("trainFeatures.csv", "wb"))
#create a csv writer for testFeatures
trainDataFile = csv.reader( open('/home/kwyn/GalaxyQuest/training_solutions_rev1.csv', 'rb') )
#Looping through the trainImgs directory
for root, dirs, files in os.walk(trainImgs):
  #sort file names into numeric order  
  files = sorted(files)
  for f in files:
    path = "/home/kwyn/GalaxyQuest/images_training_rev1/" + f
    #Reading, converting to b&w, and resizing to 50x50
    image = io.imread(path)
    resizeimage = resize(image, (50,50))
    gimg = color.colorconv.rgb2grey(resizeimage)   
    #Vectorizing
    i = np.vstack(gimg)       
    flat = i.flatten()
    print flat
    trainFeatures.writerow(flat)