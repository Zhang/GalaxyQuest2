# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:08:27 2014

@author: kwyn
"""

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
features_raw = pd.read_csv("/home/kwyn/GalaxyQuest/Solutions/submission1.csv", delimiter=',')
###############################################################

###############################################################
#Reads results from training data
data_raw = pd.read_csv("/home/kwyn/GalaxyQuest/TrainingData/training_solutions_rev1.csv", delimiter=',',index_col=0)
###############################################################

for i in features_raw[0:2]:
  for x in i[0:5]:
    print type(x)
    
for j in data_raw[0:2]:
  for y in j[0:5]:
    print type(y)