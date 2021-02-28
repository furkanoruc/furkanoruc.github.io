#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""
the_list = []
holder = []
num = eval(input("Enter the number of elements of the list: "))

for i in range (num):
    the_list.append(eval(input("Enter the list of integers: ")))
    
k = num    
while k-1 >= 0:
    k = k - 1
    holder.append(the_list[k])


print(holder)
