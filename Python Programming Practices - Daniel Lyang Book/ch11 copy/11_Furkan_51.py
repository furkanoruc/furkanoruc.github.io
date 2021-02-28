#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""
"""
l1 = []*2
l2 = []*2
l3 = []*2
l4 = []*2
"""
#for i in range(2):
#    l1.append(input("Enter 4 Students and their Grades on the same row, via comma separation: "))
    


l1 = ["John", 34]
l2 = ["Jim", 45]
l3 = ["Peter", 45]
l4 = ["Tim", 45]

lst = [l1,l2,l3,l4]

def bubble_sort(ls,n):
    for i in range (n-1):
        for j in range(0, n-i):
            if ls[i][1] > ls[i+1][1]:
                ls[i+1][1], ls[i][1] = ls[i][1], ls[i+1][1]
                ls[i+1][0], ls[i][0] = ls[i][0], ls[i+1][0]
    return ls

print(bubble_sort(lst, 4))

