#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

import math

class Point:
    def __init__(self,  a, b, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__a = a
        self.__b = b
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
        
    def distance(self):
        m = ((self.__x)-(self.__a))**2
        n = ((self.__y)-(self.__b))**2
        return (m+n)**(0.5)
    
    def isnearby(self):
        m = ((self.__x)-(self.__a))**2
        n = ((self.__y)-(self.__b))**2
        if (m+n)**(0.5) < 5:
            return print("Points are near each other")
        else:
            return print("Points are not near each other")
    
    def __str__(self):
        return print("(" + str(self.__x) + ")" + "(" + str(self.__y) + ")") 
    

x, y = eval(input("Enter the first point: "))
a, b = eval(input("Enter the second point: "))

result = Point(a, b, x, y)

print(result.distance())
result.isnearby()
print("String Expression: ")
(result.__str__())


    
    
    
    
    
    
    
    