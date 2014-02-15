# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:35:07 2014

@author: kwyn
"""

#Require the necessary modules
import os
import csv as csv
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
import codecs

#Define the output array
images = []
#create a csv reader for test data
#create a csv reader for trainFeatures
features_raw = open("/home/kwyn/GalaxyQuest/trainFeatures.csv", "rU")
testFeatures = csv.reader((line.replace('\0','') for line in features_raw), delimiter=",")
testFeatures = list(testFeatures)

#conver data to np array
testFeatures = np.array(trainFeatures)
#defining our randomforest regressor as rfg

##############################################
#TODO: import from joblib old algorithm
##############################################
rfr.predict(testFeatures)
