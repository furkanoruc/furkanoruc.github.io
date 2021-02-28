#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

import math

#scissor (0), rock (1), paper (2)

year = eval(input("Enter Year: "))
month = eval(input("Enter Month: "))
day_month = eval(input("Enter Day of the Month: "))
#day_week = eval(input("Day of the Week: "))


week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]




if month ==1:
    m = 13
    year = year - 1
if month == 2:
    m = 14
    year = year - 1
else:
    month = m
    

    
j = year // 100
k = year & 100
q = day_month
    

h = (q + ((26*(m+1))/10) + k + (k/4) + (j/4) + 5*j)%7


print("Day of the week is " + str(week[int(h)]))
