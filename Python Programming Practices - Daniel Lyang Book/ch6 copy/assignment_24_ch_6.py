#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random


def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime return False # number is not a prime
            
            return False
        divisor += 1
    return True

###

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
    

def combo():
    combo_list = []
    count = 0
    n = 2
    while len(combo_list) <= 100:
        
        if isPrime(n) == True and ispalindrome(n) == True:
            combo_list.append(n)
        n += 1
        count += 1
    return combo_list

combo_list = combo()


for i in range (0, 10):
    for j in range (0, 10):
        print(format(combo_list[j+i*10]), end=(" "))
    #for j in range (1,i+1):
        #print(format(j), end=(""))
    print("\r")



















