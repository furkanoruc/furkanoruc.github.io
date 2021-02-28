#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

n1 = eval(input("Enter number of integers for the 1st list: "))
number1 = []
for i in range(n1):
    number1.append(eval(input("Enter the 1st sorted list integers, one by one: ")))
    
n2 = eval(input("Enter number of integers for the 2nd list: "))
number2 = []
for i in range(n2):
    number2.append(eval(input("Enter the 2nd sorted list integers, one by one: ")))


def insertionSort(lst):
    for i in range (1,len(lst)):
        current = lst[i]
        k = i-1
        while k >= 0 and lst[k]>current:
            lst[k+1] = lst[k]
            k = k - 1
        #lst[k+1] = current
    return lst

def merge(list1, list2):
    list1.extend(list2)
    insertionSort(list1)
    return list1

print(merge(number1, number2))

#insertionSort([1,6,324,34,234,324,324,24,2,422,33,54,4,54542,2])

