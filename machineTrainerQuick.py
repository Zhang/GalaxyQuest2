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
# Define training set
'''
solutionfilename = 'Solutions/output.csv'
rfrdump = 'Algorithms/rfrdump-allfeatsnotresized'
preddump = 'Solutions/preddump'
'''
###############################################################
#Reads features from training data

feat = joblib.load('/home/kwyn/GalaxyQuest2/Data/features/features-AllAsymDil10000')

ssimfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TRAINssim10000-38.csv', delimiter=',')
ssimfeatures = np.array(ssimfeatures_raw)

features = np.column_stack((feat, ssimfeatures[0:10000, 1:39]))
#features = feat
features.shape


###############################################################

###############################################################
#Reads results from training data

data_raw = pd.read_csv("/home/kwyn/GalaxyQuest2/TrainingData/training_solutions_rev1.csv", delimiter=',',index_col=0)
data = np.array(data_raw)
print data.shape

###############################################################

###############################################################
#Reads features from test data
'''
test_raw = pd.read_csv(testFeats, delimiter=',')
test = np.array(test_raw)
print test.shape
'''
###############################################################

###############################################################
#Generates our random forest

print 'fitting ...'
#rfr = RandomForestRegressor(n_estimators=400, max_depth=9, max_features=30, n_jobs=6)
rfr = RandomForestRegressor(n_estimators=100, max_features=50, n_jobs=6)
featureFitting = features[0:7000, 1:855]
fitData = data[0:7000]
mod = rfr.fit(featureFitting, fitData)
#joblib.dump(mod, rfrdump)

###############################################################

###############################################################
'''
print 'predicting ...'
predictData = test[0:79975, 1:406]
predict = rfr.predict(predictData)
#prediction = np.column_stack((test[0:79975, 0:1],predict))
joblib.dump(prediction, preddump)
'''
###############################################################

###############################################################
#Writing data to csv using numpy.savetext
'''
print 'writing ...'
galIDs = test[:,0]
prediction = np.column_stack(galIDs, predict)
headerRow = 'GalaxyID,Class1.1,Class1.2,Class1.3,Class2.1,Class2.2,Class3.1,Class3.2,Class4.1,Class4.2,Class5.1,Class5.2,Class5.3,Class5.4	,Class6.1,Class6.2,Class7.1,Class7.2,Class7.3,Class8.1,Class8.2,Class8.3,Class8.4,Class8.5,Class8.6,Class8.7,Class9.1,Class9.2,Class9.3,Class10.1,Class10.2,Class10.3,Class11.1,Class11.2,Class11.3,Class11.4,Class11.5,Class11.6'
formatting = '%d,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f,$f'
np.savetext(solutionfilename, prediction. fmt=formatting, delimiter=',', newline='\n', header=headerRow, footer='', comments='')
'''
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

samplePredictions = rfr.predict(features[7000:10000, 1:855])
print samplePredictions.shape
print sqrt(mean_squared_error(data[7000:10000], samplePredictions))

###############################################################
