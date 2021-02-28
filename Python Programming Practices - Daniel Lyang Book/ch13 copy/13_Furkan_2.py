#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""



the_file = open("Score", "r")
lst = []
count_line = 0
count_word = 0
count_char = 0
for line in the_file:
    count_line += 1
    words = line.split()
    for word in words:
        count_word += 1
    for char in line:
        count_char += 1
        #if 
the_file.close()

print("Line: " +str(count_line))
print("Word: " + str(count_word))
print("Char: " + str(count_char))

