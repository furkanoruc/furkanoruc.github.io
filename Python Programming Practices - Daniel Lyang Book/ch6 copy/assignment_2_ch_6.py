#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

#scissor (0), rock (1), paper (2)


num = eval(input("Enter the number for sum of its digits: "))

def sumdigits(number):
    k = 0
    x = []
    summer = 0
    while number > 0:
        x.append(number % 10)
        number = (number - x[k]) // 10
        k = k + 1
    for i in range (len(x)):
        summer += x[i]
    return summer


print(sumdigits(num))
        
