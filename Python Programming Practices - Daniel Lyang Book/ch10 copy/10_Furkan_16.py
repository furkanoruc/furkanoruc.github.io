#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

#Bubble Sort!

n = 10
number = []
counter = [0] * n
for i in range(n):
    number.append(eval(input("Enter the integers, one by one: ")))

def bubble(num):
    for i in range(len(num)):
        for j in range (0, len(num)-1-i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

print(bubble(number))
