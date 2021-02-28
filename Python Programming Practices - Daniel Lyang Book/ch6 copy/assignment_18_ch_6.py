#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

number = eval(input("enter the number: "))

def printMatrix(n):
    for i in range (n):
        
        for j in range (n):
            print(random.randint(0,1), end=" ")
        print()
    return

printMatrix(number)
