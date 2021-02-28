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

number = eval(input("Enter a number between 1 to 15: "))
k = number
for i in range (1, number+1):
    for j in range (1, k):
        print (end = " ")
    k = k-1
    for j in range (1,i+1):
        print(format(i+1-j), end=(""))
    for j in range (1,i+1):
        print(format(j), end=(""))
    print("\r")
        
    