# -*- coding: utf-8 -*-
"""
Trainer
Created on Fri Feb 14 12:17:03 2014

@author: kwyn
"""

#Require the necessary modules
import csv as csv
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib


#create a csv reader for trainFeatures
features_raw = open("/home/kwyn/GalaxyQuest/trainFeatures.csv", "rU")
features = csv.reader((line.replace('\0','') for line in features_raw), delimiter=",")
features = list(features)
print
data_raw = open("/home/kwyn/GalaxyQuest/training_solutions_rev1.csv", "rU")
data = csv.reader((line.replace('\0','') for line in data_raw), delimiter=",")
data = list(data)
#convert data to np array
features = np.array(features)
data = np.array(data)
#defining our randomforest regressor as rfg
rfr = RandomForestRegressor(n_estimators=10)
rfr.fit(features,data)

joblib.dump(rfr, 'trainedRFR.pkl')
