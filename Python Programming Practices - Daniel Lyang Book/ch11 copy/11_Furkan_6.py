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


def entry_zero(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix



def multiplyMatrix(m1,m2,m3,n):
    for i in range(n):
        for j in range(n):
            summer = 0
            for k in range(n):
                summer += m1[i][k] * m2[k][j] 
            m3[i][j] = summer
    return m3

print("\nResult: \n" +str(multiplyMatrix(entry(3),entry(3),entry_zero(3),3)))

