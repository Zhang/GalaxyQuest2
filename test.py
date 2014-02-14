# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:35:07 2014

@author: kwyn
"""

#Require the necessary modules
import os
import csv as csv
import numpy as np
from skimage import io
from skimage import color
from skimage.transform import resize
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

#Define the output array
images = []
#Training pics library
trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1"


#Looping through the directory
for root, dirs, files in os.walk(trainImgs):
  #sort file names into numeric order  
  files = sorted(files)
  for f in files[0:10]:
    path = "/home/kwyn/GalaxyQuest/images_training_rev1/" + f
    #Reading, converting to b&w, and resizing to 50x50
    image = io.imread(path)
    resizeimage = resize(image, (50,50))
    gimg = color.colorconv.rgb2grey(resizeimage)   
    #Vectorizing
    i = np.vstack(gimg)       
    flat = i.flatten()
    #Pushing into result array
    images.append(flat)
    print(f)

#Read our test results data from csv
csv_file_object = csv.reader( open('/home/kwyn/GalaxyQuest/training_solutions_rev1.csv', 'rb') )

trainData = []
for row in csv_file_object:
  trainData.append(row)
#remove header row
trainData.pop(0)
#conver data to np array
trainData = np.array(data)
#defining our randomforest regressor as rfg
rfg = RandomForestRegressor(n_estimators=10)
rfg.fit(images,data)

joblib.dump(images, 'processedImages.pkl')
joblib.dump(rfg, 'firstTry.pkl')
