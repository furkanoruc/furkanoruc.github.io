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


def mean(number):
    summer = 0
    for i in range(len(number)):
        summer += number[i]
    m = summer/(len(number))
    return m

def deviation(number):
    summer = 0
    for i in range(len(number)):
        summer += (number[i] - mean(number))**2
    sd = (summer/(n-1))**(0.5)
    return sd

print("The S.D. is: "+ str(deviation(number)))
print("The mean is: "+ str(mean(number)))
