#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import turtle
import math

number_of_students = eval(input("Enter number of students: "))
note_list = [] * number_of_students

for i in range (0, number_of_students):
    x = eval(input("Enter student " + str(i+1) + "'s score : "))
    note_list.append(x)
    
    
for i in range (len(note_list)):
    for j in range (len(note_list)):
        if i != j:
            if note_list[i] < note_list[j]:
                note_list[j], note_list[i] = note_list[i], note_list[j]


print("\nTop highest scores is: "+str(note_list[number_of_students-1]))
print("2n highest scores is: "+str(note_list[number_of_students-2]))

