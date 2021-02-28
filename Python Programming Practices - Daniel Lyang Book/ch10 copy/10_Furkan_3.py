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

for i in range(len(number)):
    for j in range (0,len(number)):
        if number[i] == number[j]:
            counter[i] += 1

#print(counter)

#for i in range (len(number)):

number2 = set(number)
number2 = list(number2)
cc = [0]*len(number2)
for i in range(len(number)):
    for j in range(len(number2)):
        if number[i] == number2[j]:
            cc[j] = counter[i]
    
#print(number2)
#print(cc)

for i in range(len(number2)):
    print(str(number2[i])+ " occur/occurs " + str(cc[i]) + " times")
