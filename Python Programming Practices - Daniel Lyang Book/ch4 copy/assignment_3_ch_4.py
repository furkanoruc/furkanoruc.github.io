#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


a,b,c,d,e,f = eval(input("Enter a, b, c, d, e, f: "))


if a*d - b*c == 0:
    print("The equation has no solution.")
    
else:
    x = (e*d-b*f)/(a*d-b*c)
    y = (a*f-e*c)/(a*d-b*c)

print("x is: " + str(x))
print("y is: " + str(y))





