#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""
import random
lst = [0]* 8
j = 0
lst[0] = random.randint(0,8)
for i in range(0,len(lst)-1):
        for j in range(0, len(lst)):
            if lst[j] != j + 1 and lst[j] != j -1 and j!=lst[i]:
                lst[i+1] = j

print(lst)
