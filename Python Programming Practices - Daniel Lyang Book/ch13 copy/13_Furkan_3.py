#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

#f = open('./q3_grades.txt','w')
"""
import random
for i in range(70):
    print(random.randint(10,100))
"""

the_file = open("q3_grades.txt", "r")

lst = []

for line in the_file:
    for num in line.split():
        lst.append(eval(num))

summer = 0
for i in range(len(lst)):
    summer += lst[i]

mean = summer/len(lst)

print("Total number of scores: " + str(len(lst)))
print("Average: " + str(mean))
print("Total: " + str(summer))
