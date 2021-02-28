#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

n = eval(input("Enter number of integers: "))
number = []
counter = [0] * n
for i in range(n):
    number.append(eval(input("Enter the integers, one by one: ")))


def sorted(num):
    count = 0
    for i in range(len(num)):
        if num[i] > num[i+1]:
            break
        else:
            count += 1
    if count == len(num):
        return print("Sorted")
    else:
        return print("Not Sorted")
    
sorted(number)