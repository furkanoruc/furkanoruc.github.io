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


#function for sum of a list
def summer(list1):
    total = 0
    for i in range(0, len(list1)):
        total = total + list1[i]
    return total


perfect = []


for j in range (1,10000):
    gcd = []
    for i in range (1,j):
        if j % i == 0:
            gcd.append(i)
    if summer(gcd) == j:
        perfect.append(j)
    
    
print(perfect)

