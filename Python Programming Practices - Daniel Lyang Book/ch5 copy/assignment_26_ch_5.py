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

sum = 0
for i in range (1,97,2):
    x = i
    y = i + 2
    #print(x/y)
    sum = sum + x/y
    
print(sum)