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

# Files to use 
#trainFeats = "/home/kwyn/GalaxyQuest2/Data/TrainAllFeaturesNotResized.csv"
trainSols = "/home/kwyn/GalaxyQuest2/TrainingData/training_solutions_rev1.csv"
#testFeats = "/home/kwyn/GalaxyQuest2/Data/TestAllFeaturesNotResized.csv"

# number of features extracted
#numFeatures = 22501

solutionfilename = 'Solutions/TestResults-AllAsymDil.csv'
rfrdump = 'Algorithms/rfr-AllAsymDil'
preddump = 'Predictions/pred-AllAsymDil'

###############################################################
#Reads features from training data

'''
print 'reading allfeatures ...'
allfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TRAINAllFeatures.csv', delimiter=',')
allfeatures = np.array(allfeatures_raw)
allfeatures.shape

print 'reading brightnessRatio ...'
brfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TRAINbrightnessRatioFeatures.csv', delimiter=',')
brfeatures = np.array(brfeatures_raw)
brfeatures.shape

print 'combining ...'
featsub1 = np.column_stack((allfeatures, brfeatures[0:61578, 1:1]))

'''

#features_raw = joblib.load('/home/kwyn/GalaxyQuest2/Data/features/features-AllAsymDilBR')
features_raw = joblib.load('/home/kwyn/GalaxyQuest2/Data/features/features-AllAsymDil')
features = np.array(features_raw)

###############################################################

###############################################################
#Reads results from training data

'''
data_raw = pd.read_csv(trainSols, delimiter=',',index_col=0)
=======
data_raw = pd.read_csv("/Users/hackreactor1/Desktop/GalaxyQuest2/training_solutions_rev1.csv", delimiter=',',index_col=0)
>>>>>>> add300cb0cca1eb7ed212b9058dd2c6d7be609f1
data = np.array(data_raw)
print data.shape
'''
###############################################################

###############################################################
#Reads features from test data


'''
tallfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TESTAllFeatures.csv', delimiter=',')
tallfeatures = np.array(tallfeatures_raw)

tasymfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TESTAsymFeatures.csv', delimiter=',')
tasymfeatures = np.array(tasymfeatures_raw)

featsub2 = np.column_stack((tallfeatures, tasymfeatures[0:79975, 1:7]))

tdilfeatures_raw = pd.read_csv('/home/kwyn/GalaxyQuest2/Data/TESTDilationFeatures.csv', delimiter=',')
tdilfeatures = np.array(tdilfeatures_raw)

featsub23 = np.column_stack((featsub2, tdilfeatures[0:79975, 1:401]))

joblib.dump(featsub23, '/home/kwyn/GalaxyQuest2/Data/features/features-TESTAllAsymDil')

test_raw = joblib.load('/home/kwyn/GalaxyQuest2/Data/features/features-TESTAllAsymDil')
#test_raw = pd.read_csv(testFeats, delimiter=',')
test = np.array(test_raw)
print test.shape
'''
###############################################################

###############################################################
#Generates our random forest
'''
print 'fitting ...'
#rfr = RandomForestRegressor(n_estimators=400, max_depth=9, max_features=30, n_jobs=6)
rfr = RandomForestRegressor(n_estimators=400, max_features=200, n_jobs=6)
#featureFitting = features[0:61578, 1:814]
#fitData = data[0:61578]
featureFitting = features[0:54000, 1:814]
fitData = data[0:54000]
mod = rfr.fit(featureFitting, fitData)
joblib.dump(mod, rfrdump)
'''
###############################################################

###############################################################
'''
print 'predicting ...'
predictData = test[0:79975, 1:814]
predict = rfr.predict(predictData)
#prediction = np.column_stack((test[0:79975, 0:1],predict))
joblib.dump(prediction, preddump)

###############################################################

###############################################################
#Writing data to csv using numpy.savetext

print 'writing ...'
galIDs = test[:,0]
prediction = np.column_stack(galIDs, predict)
headerRow = 'GalaxyID,Class1.1,Class1.2,Class1.3,Class2.1,Class2.2,Class3.1,Class3.2,Class4.1,Class4.2,Class5.1,Class5.2,Class5.3,Class5.4	,Class6.1,Class6.2,Class7.1,Class7.2,Class7.3,Class8.1,Class8.2,Class8.3,Class8.4,Class8.5,Class8.6,Class8.7,Class9.1,Class9.2,Class9.3,Class10.1,Class10.2,Class10.3,Class11.1,Class11.2,Class11.3,Class11.4,Class11.5,Class11.6'
formatting = '%d,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f.%f,%f,%f,%f,%f,$f'
np.savetext(solutionfilename, prediction, fmt=formatting, delimiter=',', newline='\n', header=headerRow, footer='', comments='')
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
'''
samplePredictions = rfr.predict(features[54000:60000, 1:814])
print samplePredictions.shape
print sqrt(mean_squared_error(data[54000:60000], samplePredictions))
'''
###############################################################
