# -*- coding: utf-8 -*-
"""
Trainer
Created on Fri Feb 14 12:17:03 2014

@author: kwyn
"""
#Require the necessary modules
import time
import csv as csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
from sklearn import cross_validation
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from math import sqrt

###############################################################
#Reads features from training data
features_raw = pd.read_csv("/home/kwyn/GalaxyQuest/Data/Test4.csv", delimiter=',')
features = np.array(features_raw)
print features.shape
###############################################################

###############################################################
#Reads results from training data
data_raw = pd.read_csv("/home/kwyn/GalaxyQuest/TrainingData/training_solutions_rev1.csv", delimiter=',',index_col=0)
data = np.array(data_raw)
print data.shape
###############################################################

###############################################################
#Reads features from test data
test_raw = pd.read_csv("/home/kwyn/GalaxyQuest/Data/TestMe.csv", delimiter=',')
test = np.array(test_raw)
print test.shape
###############################################################

###############################################################
#Generates our random forest

rfr = RandomForestRegressor(n_estimators=400, max_depth=9, max_features=30, n_jobs=6)
featureFitting = features[0:10000, 1:406]
fitData = data[0:10000]
rfr.fit(featureFitting, fitData)

###############################################################

###############################################################

predictData = test[0:79975, 1:406]
predict = rfr.predict(predictData)
prediction = np.column_stack((test[0:79975, 0:1],predict))
joblib.dump(prediction, 'Solutions/output')

###############################################################

###############################################################
#Writing data to csv
'''
with open('Solutions/TestSubmission.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
  for x in range(test.shape[0]):
    y = test[x][1:205]
    idName = np.array(int(test[0][0]))
    prediction = rfr.predict(y)
    final = np.append(idName , prediction)
    writer.writerow(final)
'''
###############################################################

###############################################################
#Testing our model against training data
'''
samplePredictions = rfr.predict(features[7000:10000, 1:406])
print samplePredictions.shape
print sqrt(mean_squared_error(data[7000:10000], samplePredictions))
'''
###############################################################
