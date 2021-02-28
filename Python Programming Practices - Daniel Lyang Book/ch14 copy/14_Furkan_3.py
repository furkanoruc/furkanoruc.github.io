#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

filename = input("Enter the filename: ")

#f = open("Score copy",'r')

f = open(filename,'r')

a = str()
for line in f:
    for word in line.split():
        a += word + " "

lst = []
k = 0

st = a.split()
for i in st:
    if i not in lst:
        lst.append(i)
        
for i in range (0, len(lst)):
    print("Frequency of: ", lst[i], "is: ", st.count(lst[i]))
    


