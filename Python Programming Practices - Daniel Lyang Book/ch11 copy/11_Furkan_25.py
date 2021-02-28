#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

import random

def entry_random(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0,1))
    return matrix

def entry(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(eval(
                input("Enter elements of the matrix, row by row: ")))
    return matrix


#n=3 for our case.
    
def ismarkov(m,n):
    count = 0
    for i in range(n):
        summer = 0
        for j in range(n):
            if m[i][j] < 0:
                return "Non Markov"
            else:
                summer += m[j][i]
                if j==n-1 and summer == 1:
                    count += 1
    if count == 3:
        return "Markov"
    else: 
        return "Non Markov"


print(ismarkov(entry(3), 3))







                