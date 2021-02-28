#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

def entry(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(eval(
                input("Enter elements of the matrix, row by row: ")))
    return matrix


#entry(3)
   
def entry_zero(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix


def sumMatrix(m1, m2, m3, n):     
    for i in range(n):
        for j in range(n):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3


print(sumMatrix(entry(3), entry(3), entry_zero(3), 3))
