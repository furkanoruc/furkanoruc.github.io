#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

str_1 = input("Enter str 1 (The Substring Candidate): ")

str_2 = input("Enter str 2 (The Superstring Candidate): ")

def measure(s1, s2):
    count = 0
    for i in range(len(s1)):
        for j in range(i, len(s2)):
            if i == j:
                count += 1
    if count == len(s1):
        print("Substring!")
    else:
        print("Not Substring!")
    
measure(str_1, str_2)
