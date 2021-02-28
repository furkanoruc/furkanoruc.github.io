#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random


a, b, c = eval(input("Enter three numbers to be ordered: "))

#Palindrome

def more(x,y,z):
    if x > y:
        if x > z:
            x1 = x
        if z > x:
            x1 = z
        if z > y:
            x2 = z
            x3 = y
        if y > z:
            x2 = y
            x3 = z
    if y > x:
        if y > z:
            x1 = y
        if z > y:
            x1 = z
        if z > x:
            x2 = z
            x3 = x
        if x > z:
            x2 = x
            x3 = z
            
    return x3,x2,x1


print(more(a,b,c))

#print(more(10,20))

