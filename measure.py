# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:53:44 2014

@author: kwyn
"""
import os
import csv as csv
import numpy as np
from skimage import io
from skimage.transform import resize
from sklearn.externals import joblib
from PIL import Image
import csv
from skimage import data, filter, color
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
import scipy
import math
from math import sqrt
from skimage import img_as_float
from skimage.measure import structural_similarity as ssim

###############################################################
trainImgs = '/home/kwyn/GalaxyQuest2/images_training_rev1/'
testImgs = '/home/kwyn/GalaxyQuest2/images_test_rev1/'
inputImgs = trainImgs

outputFilename = '/home/kwyn/GalaxyQuest2/Data/TRAINssim10000-38.csv'

numFeatures = 39

#Don't forget to change the file range in line 85 (for f in files[0:1000]:)

###############################################################
'''
#img = data.camera()
img2 = io.imread(inputImgs+'105797.jpg', as_grey=True)
#print img.shape, img2.shape
ssim11 = ssim(img2, img2, dynamic_range=img2.max() - img2.min())
print ssim11
'''
path = inputImgs

#>98% 1.1

path11 = path + '105797.jpg'
path12 = path + '106040.jpg'
path13 = path + '107619.jpg'
#>98% 1.2
path21 = path + '102243.jpg'
path22 = path + '102402.jpg'
path23 = path + '103533.jpg'

path31 = path + '205541.jpg'
path32 = path + '185561.jpg'
path41 = path + '185561.jpg'
path42 = path + '780966.jpg'
path51 = path + '454627.jpg'
path52 = path + '706376.jpg'
path53 = path + '180894.jpg'
path54 = path + '877297.jpg'
path61 = path + '579750.jpg'
path62 = path + '627799.jpg'
path71 = path + '585988.jpg'
path72 = path + '545652.jpg'
path73 = path + '834060.jpg'
path81 = path + '478315.jpg'
path82 = path + '608304.jpg'
path83 = path + '869304.jpg'
path84 = path + '662018.jpg'
path85 = path + '471591.jpg'
path86 = path + '373505.jpg'
path87 = path + '868815.jpg'
path91 = path + '827293.jpg'
path92 = path + '162557.jpg'
path93 = path + '107454.jpg'
path101 = path + '309198.jpg'
path102 = path + '121394.jpg'
path103 = path + '416488.jpg'
path111 = path + '848818.jpg'
path112 = path + '807715.jpg'
path113 = path + '121006.jpg'
path114 = path + '233081.jpg'
path115 = path + '495381.jpg'
path116 = path + '598442.jpg'


pathnew = path + '103610.jpg'

img11 = io.imread(path11, as_grey=True)
img11 = img11[137:287, 137:287]
#img11 = img_as_float(img)
img12 = io.imread(path12, as_grey=True)
img12 = img12[137:287, 137:287]
#img12 = img_as_float(img)
img13 = io.imread(path13, as_grey=True)
img13 = img13[137:287, 137:287]

img21 = io.imread(path21, as_grey=True)
img21 = img21[137:287, 137:287]

img22 = io.imread(path22, as_grey=True)
img22 = img22[137:287, 137:287]

img23 = io.imread(path23, as_grey=True)
img23 = img23[137:287, 137:287]

#############################

img31 = io.imread(path31, as_grey=True)
img31 = img31[137:287, 137:287]

img32 = io.imread(path32, as_grey=True)
img32 = img32[137:287, 137:287]

img41 = io.imread(path41, as_grey=True)
img41 = img41[137:287, 137:287]

img42 = io.imread(path42, as_grey=True)
img42 = img42[137:287, 137:287]

img51 = io.imread(path51, as_grey=True)
img51 = img51[137:287, 137:287]

img52 = io.imread(path52, as_grey=True)
img52 = img52[137:287, 137:287]

img53 = io.imread(path53, as_grey=True)
img53 = img53[137:287, 137:287]

img54 = io.imread(path54, as_grey=True)
img54 = img54[137:287, 137:287]

img61 = io.imread(path61, as_grey=True)
img61 = img61[137:287, 137:287]

img62 = io.imread(path62, as_grey=True)
img62 = img62[137:287, 137:287]

img71 = io.imread(path71, as_grey=True)
img71 = img71[137:287, 137:287]

img72 = io.imread(path72, as_grey=True)
img72 = img72[137:287, 137:287]

img73 = io.imread(path73, as_grey=True)
img73 = img73[137:287, 137:287]

img81 = io.imread(path81, as_grey=True)
img81 = img81[137:287, 137:287]

img82 = io.imread(path82, as_grey=True)
img82 = img82[137:287, 137:287]

img83 = io.imread(path83, as_grey=True)
img83 = img83[137:287, 137:287]

img84 = io.imread(path84, as_grey=True)
img84 = img84[137:287, 137:287]

img85 = io.imread(path85, as_grey=True)
img85 = img85[137:287, 137:287]

img86 = io.imread(path86, as_grey=True)
img86 = img86[137:287, 137:287]

img87 = io.imread(path87, as_grey=True)
img87 = img87[137:287, 137:287]

img91 = io.imread(path91, as_grey=True)
img91 = img91[137:287, 137:287]

img92 = io.imread(path92, as_grey=True)
img92 = img92[137:287, 137:287]

img93 = io.imread(path93, as_grey=True)
img93 = img93[137:287, 137:287]

img101 = io.imread(path101, as_grey=True)
img101 = img101[137:287, 137:287]

img102 = io.imread(path102, as_grey=True)
img102 = img102[137:287, 137:287]

img103 = io.imread(path103, as_grey=True)
img103 = img103[137:287, 137:287]

img111 = io.imread(path111, as_grey=True)
img111 = img111[137:287, 137:287]

img112 = io.imread(path112, as_grey=True)
img112 = img112[137:287, 137:287]

img113 = io.imread(path113, as_grey=True)
img113 = img113[137:287, 137:287]

img114 = io.imread(path114, as_grey=True)
img114 = img114[137:287, 137:287]

img115 = io.imread(path115, as_grey=True)
img115 = img115[137:287, 137:287]

img116 = io.imread(path116, as_grey=True)
img116 = img116[137:287, 137:287]

#############################

def ssimg(imgPath):

  img = io.imread(imgPath, as_grey=True)
  img = img[137:287, 137:287]

  ssim11 = ssim(img, img11)
  ssim12 = ssim(img, img12)
  ssim13 = ssim(img, img13)
  ssim21 = ssim(img, img21)
  ssim22 = ssim(img, img22)
  ssim23 = ssim(img, img23)
  ssim31 = ssim(img, img31)
  ssim32 = ssim(img, img32)
  ssim41 = ssim(img, img41)
  ssim42 = ssim(img, img42)
  ssim51 = ssim(img, img51)
  ssim52 = ssim(img, img52)
  ssim53 = ssim(img, img53)
  ssim54 = ssim(img, img54)
  ssim61 = ssim(img, img61)
  ssim62 = ssim(img, img62)
  ssim71 = ssim(img, img71)
  ssim72 = ssim(img, img72)
  ssim73 = ssim(img, img73)
  ssim81 = ssim(img, img81)
  ssim82 = ssim(img, img82)
  ssim83 = ssim(img, img83)
  ssim84 = ssim(img, img84)
  ssim85 = ssim(img, img85)
  ssim86 = ssim(img, img86)
  ssim87 = ssim(img, img87)
  ssim91 = ssim(img, img91)
  ssim92 = ssim(img, img92)
  ssim93 = ssim(img, img93)
  ssim101 = ssim(img, img101)
  ssim102 = ssim(img, img102)
  ssim103 = ssim(img, img103)
  ssim111 = ssim(img, img111)
  ssim112 = ssim(img, img112)
  ssim113 = ssim(img, img113)
  ssim114 = ssim(img, img114)
  ssim115 = ssim(img, img115)
  ssim116 = ssim(img, img116)
  #  classOne = ssim11 + ssim12 + ssim13
#  classTwo = ssim21 + ssim22 + ssim23
#  return classOne, classTwo
  return ssim11, ssim12, ssim13, ssim21, ssim22, ssim23, ssim31, ssim32, ssim41, ssim42, ssim51, ssim52, ssim53, ssim54, ssim61, ssim62, ssim71, ssim72, ssim73, ssim81, ssim82, ssim83, ssim84, ssim85, ssim86, ssim87, ssim91, ssim92, ssim93, ssim101, ssim102, ssim103, ssim111, ssim112, ssim113, ssim114, ssim115, ssim116

#print ssimg(pathnew)
###############################################################
#Writes features to CSV
#Path to Training pics library
#trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1/"
#Looping through the trainImgs directory

with open(outputFilename, 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  a = [0] * numFeatures
  writer.writerow(a)
  for root, dirs, files in os.walk(inputImgs):
  #sort file names into numeric order
    files = sorted(files)
    for f in files[0:10000]:
      galName = np.array(f[:-4])
      path = inputImgs + f
      s = ssimg(path)
      total = np.append(galName, s)
      writer.writerow(total)
