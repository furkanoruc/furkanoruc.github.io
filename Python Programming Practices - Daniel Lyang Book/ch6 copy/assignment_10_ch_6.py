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

def prime_hunter(x):
    count = 0
    for i in range (3,x):
        if isPrime(i) == True:
            count += 1
            #break
    return count

print(prime_hunter(10000))

#Answer : 1228



