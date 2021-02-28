#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import math

number = eval(input("Enter a 4 digit integer: "))

ones = number % 10
tens = (number - ones) % 100
hundreds = (number - tens - ones) % 1000
last = (number - hundreds - tens - ones) / 1000

one = ones
ten = tens / 10
hundred = hundreds / 100

print("The reversed number is: " + str(one) + str(int(ten)) + str(int(hundred)) + str(int(last)))




