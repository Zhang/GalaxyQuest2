"""
Convert results joblib pkl to csv for submission

@author: kwyn
"""

import time
import csv as csv
import numpy as np
from sklearn.externals import joblib
######################################
#TODO: hard code header here
#header = 
######################################

#Loads results pkl
results = np.load("Solutions/output_01.npy")
print results.shape
######################################
# finish galaxyIds.py to save this pkl. Make sure the .load points to the right file path
######################################

#Open CSV writer
with open('Solutions/submission1.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
  trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1/"
  #write each row into the CSV writer.
  for i in results:
    for root, dirs, files in os.walk(trainImgs):
      files = sorted(files)
      for f in files:
        galName = np.array(f[:-4])
        total = np.append(galName,i[1:38])
        writer.writerow(total)