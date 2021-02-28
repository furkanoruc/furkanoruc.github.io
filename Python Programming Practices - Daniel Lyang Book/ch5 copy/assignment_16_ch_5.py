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

number1, number2 = eval(input("Enter two numbers: "))

if number1 > number2:
    x = number2
else:
    x = number1

for i in range (x, 0, -1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
        break
    
print(str(i) + " is the greatest common diviser")


