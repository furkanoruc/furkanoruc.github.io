#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

n = eval(input("Enter number of rows and columns for a square matrix: "))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(eval(input("Enter elements of the matrix, row by row: ")))
        
def sumMajorDiagonal(m,n):
    x = 0
    for i in range(0, n):
        x += m[i][i]
    return x

    
print("Sum of the elements in the major diagonal are: " +
str(sumMajorDiagonal(matrix,n)))





