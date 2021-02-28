#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:03:45 2020

@author: furkanoruc
"""

import pandas as pd

df_train = pd.read_csv("train1k - Copy.csv", sep = ",")
df_test = pd.read_csv("test1k - Copy.csv", sep = ",")


  
#Creating a dataframe in order to store the means of each pixels for each numbers in the training data  
 
pixel_sum = [] 
df_pixel_sum = pd.DataFrame(pixel_sum) 
pixel_mean = [] 
df_pixel_mean = pd.DataFrame(pixel_mean) 
 
label_hold = [] 
k = 0 
label_holder = df_train["label"] 
 
for k in range (0,10): 
    df_pixel_sum[k] = df_train.loc[df_train["label"] == k ,:].sum() 
    df_pixel_mean[k] = df_train.loc[df_train["label"] == k ,:].mean() 
    k = k + 1 
 
t=0 
indexer = [] 
for t in range(785): 
    indexer.append(t) 
 
#Set mean pixel's index to numbers for easy access 
 
df_pixel_mean.set_index([indexer], inplace=True) 
 
#Nearest Mean Classifier 
 
#Right Now: Only for 0 Image & 1st Row of Test Data 
 
i = 1 
pixel_difference = [] 
number_identifier = [] 
near_mc = [] 
#assigned_instance 
df_assigned_instance = pd.DataFrame() 
df_pixel_difference = pd.DataFrame(pixel_difference) 
df_number_identifier = pd.DataFrame(number_identifier) 
df_near_mc = pd.DataFrame(near_mc) 
m = 0 
k = 0 
r = 0 
s = 0 
l = 0 
 
for r in range (0,1000): 
    for m in range (0, 10): # for each mean of each number 
        pixel_difference.clear()  
        for i in range(1, 785): # for each pixel. cover all pixels 
            pixel_difference.append((df_train.iloc[r,i] - df_pixel_mean.iloc[i, m])**2)  
        #For the 0th image in test data, subtract and square each pixel's value from each pixel's mean for each number  
            i = i + 1 
        df_pixel_difference[m] = pixel_difference # Store the calculation for each image 
     
    #for k in range (0,10): # For each number's mean, find the distance between 0th test data  
        number_identifier.append(df_pixel_difference.iloc[:, m].sum()) 
        df_number_identifier [m] = number_identifier 
        m = m + 1 
        #k = k + 1 
        number_identifier.clear() 
     
    for s in range (0,10):         # Finding the minimum distance between 0th test element and number image means                     
        near_mc.append(df_number_identifier.iloc[0,s]) 
        df_near_mc[s] = near_mc 
        near_mc.clear() 
        s = s + 1 
    df_near_mc_transpose = df_near_mc.transpose() 
         
    assigned_instance = (df_near_mc_transpose.idxmin()) 
    df_assigned_instance[r] = assigned_instance 
    #assigned_instance.clear() 
     
df_assigned_instance = df_assigned_instance.transpose() 
 
 
# Self Test for the Accuracy 
 
q = 0 
rank = 0 
 
for q in range (0,1000): 
    if df_assigned_instance.iloc[q,0] == df_train.iloc[q,0]: 
        rank = rank + 1 
print(rank) 
 
 
# Confusion matrix as 0s 
 
confusion = [0] * 10 
df_confusion_2 = pd.DataFrame(confusion) 
f = 0 
for f in range (1,10): 
    df_confusion_2[f] = df_confusion_2[0] 
     
# Create the Confusion Matrix 
 
f = 0 
x = 0 
y = 0 
 
for f in range(len(df_train)): 
     
    if df_assigned_instance.iloc[f,0] == df_train.iloc[f,0]: 
        x = df_train.iloc[f,0] 
        df_confusion_2.iloc[x,x] = df_confusion_2.iloc[x,x] + 1 
     
    elif df_assigned_instance.iloc[f,0] != df_train.iloc[f,0]: 
        y = df_train.iloc[f,0] 
        x = df_assigned_instance.iloc[f,0] 
        df_confusion_2.iloc[y,x] = df_confusion_2.iloc[y,x] + 1 
 
pixel_mean_transpose = []
df_pixel_mean_transpose = pd.DataFrame(pixel_mean_transpose)
df_pixel_mean_transpose = df_pixel_mean_transpose.transpose()

from matplotlib import pyplot
import numpy as np
import csv
import matplotlib.pyplot as plt
k = 0
for k in (0,9):
    
    label = df_pixel_mean_transpose[k]

    pixels_mean = df_pixel_mean_transpose[1:]

    pixels_mean = np.array(pixels_mean, dtype='uint8')

    deneme = pixels_mean[:,k].reshape(28, 28)

    plt.title('Label is {label}'.format(label=label))
    plt.imshow(deneme, cmap='gray')
    plt.show()
    k = k + 1
        
    
    
deneme = [] 
    
deneme = pixels_mean[:,0]

deneme.reshape(28,28)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  