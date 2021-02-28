#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

#Palindrome
def reverse(number):
    k = 0
    x = []
    new_number = 0
    while number > 0:
        x.append(number % 10)
        number = (number - x[k]) // 10
        k = k + 1
    for i in range (len(x)):
        new_number += x[i] * 10**(len(x) - i-1)
    return new_number


def ispalindrome(num2):
    if num2 - reverse(num2) == 0:
        return True
    else:
        return False
    
num = eval(input("Enter the number for palindrome: "))

print(ispalindrome(num))

