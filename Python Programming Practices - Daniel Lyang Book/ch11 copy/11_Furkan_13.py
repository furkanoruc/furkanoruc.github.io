#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

import random

def entry(n1,n2):
    matrix = []
    for i in range(n1):
        matrix.append([])
        for j in range(n2):
            matrix[i].append(eval(
                input("Enter elements of the matrix, row by row: ")))
    return matrix


def largest_element(m,n1,n2):
    largest = m[0][0]
    for i in range(n1):
        for j in range(n2):
            if m[i][j] > largest:
                largest = m[i][j]
                i_holder = i
                j_holder = j
    return i_holder, j_holder

def entry_random(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0,10))
    return matrix

x = entry(4,4)
row, column = largest_element(x, 4,4)
print(x)
print("The location of the largest element is(row, column): " 
      +str(row) + "," + str(column))

