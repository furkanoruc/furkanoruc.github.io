#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

import math

input1 = eval(input("Enter today's day: "))
input2 = eval(input("Enter the number of days elapsed since today: "))


week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

gap = input2 % 7

print("Today is " + str(week[input1] + " the future day is " + str(week[(input1+gap)%7])))