#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

import math

number1 = random.randint(0,100)
number2 = random.randint(0,100)

answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

if answer == number1 + number2:
    print("Correct!")
else:
    print("Wrong!")