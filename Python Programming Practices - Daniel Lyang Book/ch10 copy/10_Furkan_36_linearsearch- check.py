#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

#Linear Search

n = eval(input("Enter number of integers: "))
lst = []
#counter = [0] * n
for i in range(n):
    lst.append(eval(input("Enter the integers, one by one: ")))

key = eval(input("Enter the key to be searched: "))

for i in range(len(lst)):
    if key == lst[i]:
        ind = i
        break


print(lst[ind], ind)