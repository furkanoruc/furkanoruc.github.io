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

#for simplicity, each month is assumed to be 30 days total.

day = eval(input("Enter the first day of the year: "))
year = eval(input("Enter the year: "))


weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", 
          "October", "November", "December"]


for i in range (0,12):
    first = (day + i*30) % 7
    print(str(months[i] + " 1 " + str(year) + " is " + str(weeks[first])))
    
    