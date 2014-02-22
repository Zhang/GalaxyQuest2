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

###############################################################
#Gets average color
#def get_average_color((x,y), n, image):
# 
#    r, g, b = 0, 0, 0
#    count = 0
#    for s in range(x, x+n+1):
#        for t in range(y, y+n+1):
#            pixlr, pixlg, pixlb = image[s, t]
#            r += pixlr
#            g += pixlg
#            b += pixlb
#            count += 1
#    return ((r/count), (g/count), (b/count))
################################################################
##Gets brightest pixel value
#def get_brightest_pixel((x,y), n, image): 
#    brightness = 0
#    count = 0
#    for s in range(x, x+n+1):
#        for t in range(y, y+n+1):
#            pixlr, pixlg, pixlb = image[s, t]
#            brightPix = pixlr+pixlg+pixlb
#            if brightPix > brightness:
#              brightness = brightPix
#            count += 1
#    return brightness/3
################################################################
##draws core image
#def draw_core(imagePath, name): 
#  path = imagePath
#  image_rgb = io.imread(path)
#  #resizedimg = image_rgb[187:237,187:237]
#  resizedimg = image_rgb[137:287,137:287]
#  image_gray = color.rgb2gray(resizedimg)
#  edges = filter.canny(image_gray, high_threshold=0.1, sigma=5.5)
#  scipy.misc.imsave(str("actual"+name), image_rgb)    
#  scipy.misc.imsave(str("acresized"+name), resizedimg)  
#  scipy.misc.imsave(str(name), edges)
#  edges
#  #result = hough_ellipse(edges)
#  #best = result[-1]
#  #a = best[3]
#  #b = best[4]
#  #return math.pi*2*(sqrt(a**2+b**2/2))
#
################################################################
##Writes features to CSV
##Path to Training pics library
#trainImgs = "/home/kwyn/GalaxyQuest/images_training_rev1/"
##Looping through the trainImgs directory
#with open('Data/Features100.csv', 'wb') as csvfile:
#  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#  a = [0] * 406
#  writer.writerow(a)
#  for root, dirs, files in os.walk(trainImgs):
#  #sort file names into numeric order
#    files = sorted(files)
#    for f in files[0:100]:
#      galName = np.array(f[:-4])
#      path = "/home/kwyn/GalaxyQuest/images_training_rev1/" + f
#      #draw_core(path, f[:-4] +"inner.jpg")
#      img = Image.open(path).load()
#      imgAvgColor = get_average_color((162,162),100,img)
#      averageBrightness = np.array([sum(imgAvgColor)/3])
#      brightestPixel = get_brightest_pixel((162,162),100,img)
#      img = io.imread(path)
#      resizedimg = img[137:287,137:287]
#      gimg = color.colorconv.rgb2grey(resizedimg)
#      resized = resize(gimg, (20,20))
#      i = np.vstack(resized)
#      flat = i.flatten()
#      total = np.append(galName, np.append(flat,np.append(imgAvgColor, np.append(averageBrightness, brightestPixel))))
#      writer.writerow(total)


#############################################################
#Path to Training pics Library
trainImgs = "/Users/sonali/Desktop/Copy/HackReactor/GalaxyQuest2/images/image1.jpg"
#Working, but Y lines (450) are in different format as X lines (3x150).
def asymmetry(image):
  img = Image.open(image).convert('RGB')
  resizedimg = img.crop((138,138,288,288))
  rotated90 = resizedimg.rotate(90)
  rotated180 = resizedimg.rotate(180)
  imgArr1 = np.array(resizedimg)
  imgArr2 = np.array(rotated90)
  imgArr3 = np.array(rotated180)
  originalX = imgArr1[75]
  rotated90X = imgArr2[75]
  rotated180X = imgArr3[75]
  for i in range(imgArr1.shape[0]):
      if i == 0:
          originalY = imgArr1[i][75]
      else:
          originalY = np.append(originalY, imgArr1[i][75])
  for i in range(imgArr2.shape[0]):
      if i == 0:
          rotated90Y = imgArr2[i][75]
      else:
          rotated90Y = np.append(rotated90Y, imgArr2[i][75])
  for i in range(imgArr3.shape[0]):
    if i == 0:
        rotated180Y = imgArr3[i][75]
    else:
        rotated180Y = np.append(rotated180Y, imgArr3[i][75])

asymmetry(trainImgs)
##############################################################
#Finds total brightness of entire image
#x and y are starting pixel coordinates of image
#n is distance from starting point to endpoint
def totalBrightness((x,y), n, image):
    brightness = 0

    for s in range(x, x+n):
        for t in range(y, y+n):
            pixlr, pixlg, pixlb = image.getpixel((s,t))
            brightness += pixlr+pixlg+pixlb
    brightnessTotal = brightness/3
    return brightnessTotal

##############################################################
#Finds ratio of area containing 75% of image's total brightness to area containing 25% of total brightness    
def brightnessRatios(image):
    img = Image.open(image).convert('RGB')
    resizedimg = img.crop((138,138,288,288)) 
    brightnessTotal = totalBrightness((0,0), 150, resizedimg)
    sections = []
#    distance25 = 0
    for i in range(1,75):
        section25 = resizedimg.crop((75-i, 75-i, 75+i, 75+i))
        if totalBrightness((0,0),2*i,section25) >= brightnessTotal * 0.25:
            sections.append(i+1)
            distance25 = i
            break
    for i in range(distance25, 75):
        section75 = resizedimg.crop((75-i, 75-i, 75+i, 75+i)) 
        if totalBrightness((0,0),2*i,section75) >= brightnessTotal * 0.75:
            sections.append(i+1)
            break
        if i == 74:
            sections.append(i+1)
    brightnessRatio = sections[1]/float(sections[0])
    return brightnessRatio

trainImgs = "/Users/sonali/Desktop/Copy/HackReactor/GalaxyQuest2/images/image1.jpg"
brightnessRatios(trainImgs)
