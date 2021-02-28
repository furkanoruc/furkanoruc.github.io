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

#print(entry_random(4))

def row_column_finder(m, n):
    row_count = [0]*4
    column_count = [0]*4
    for i in range (n):
        for j in range(n):
            if m[i][j] == 1:
                row_count[i] += 1
                column_count[j] += 1
    return row_count, column_count,m


rows, columns, ma = row_column_finder(entry_random(4), 4)

#print(ma)
print(rows)
print(columns)


def max_2(x):
    maxer = 0
    holder = 0
    for i in range (len(x)):
        if x[i] >= maxer:
            maxer = x[i]
            holder= i
    return holder


rower = max_2(rows)
columner = max_2(columns)

print(rower)
print(columner)





