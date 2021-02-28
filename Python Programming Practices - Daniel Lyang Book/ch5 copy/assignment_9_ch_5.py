#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import turtle
import math

tuition = 10000
increase = 0.05

tuition_list = []
tuition_list.append(tuition)
for i in range (1,11):
    tuition_list.append(tuition*increase + tuition)
    tuition = tuition*increase + tuition
    if i >= 3:
        print("4 Year Tuition fee beginning with the year " + str(i-3) 
              + " is equal to " 
              + str(sum(tuition_list[i-3:i+1])))