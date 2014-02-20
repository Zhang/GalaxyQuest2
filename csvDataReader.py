"""
CSV conversion to python object

@author: Kwyn
"""
import time
import csv as csv
import numpy as np
from sklearn.externals import joblib

###############################################################
#in sublime highlight filename and press Ctrl+D repeatedly until
#everything is selected and 
#replace with the name of the csv you want to conver to a pkl
print "opening filename.csv"
filename_raw = open("/home/kwyn/GalaxyQuest/filename.csv", "rU")
filename = csv.reader((line.replace('\0','') for line in filename_raw), delimiter=",")
filename = list(filename)
filename_raw.close
filename = np.array(filename)
print "closed filename.csv"
joblib.dump(rfr, 'Data/filename.pkl')

###############################################################