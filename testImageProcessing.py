# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:48:57 2014

@author: kwyn
"""
import os
import csv as csv
import numpy as np
from skimage import io
from skimage import color
from skimage.transform import resize
#Training pics library
testImgs = "/home/kwyn/GalaxyQuest/images_test_rev1"
#create a csv reader for trainFeatures
testFeatures = csv.writer(open("testFeatures.csv", "wb"))
#Looping through the trainImgs directory
for root, dirs, files in os.walk(testImgs):
  #sort file names into numeric order  
  files = sorted(files)
  for f in files:
  	#navigate to proper file
    path = "/home/kwyn/GalaxyQuest/images_test_rev1/" + f
    #Reading, converting to b&w, and resizing to 50x50
    image = io.imread(path)
    resizeimage = resize(image, (50,50))
    gimg = color.colorconv.rgb2grey(resizeimage)   
    #Vectorizing
    i = np.vstack(gimg)       
    flat = i.flatten()
    print flat  
    #write to file
    testFeatures.writerow(flat)