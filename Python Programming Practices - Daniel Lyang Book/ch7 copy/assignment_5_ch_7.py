#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import math

class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getN(self):
        return self.__n
    
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setN(self, n):
        self.__n = n
    
    def setSide(self, side):
        self.__side = side
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def getPerimeter(self):
        perimeter = self.__n * self.__side
        return perimeter
    
    def getArea(self):
        area = (self.__n * self.__side**2) / (4* math.tan(3.14/self.__n))
        return area
    
    

poly_1 = RegularPolygon()
poly_2 = RegularPolygon(6,4)
poly_3 = RegularPolygon(10, 4, 5.6, 7.8)

print("Perimeters:")
print(poly_1.getPerimeter())
print(poly_2.getPerimeter())
print(poly_3.getPerimeter())

print("Areas:")
print(poly_1.getArea())
print(poly_2.getArea())
print(poly_3.getArea())








