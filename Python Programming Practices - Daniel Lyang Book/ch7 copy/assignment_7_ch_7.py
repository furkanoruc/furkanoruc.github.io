#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import math

class LinearEquation:
    def __init__(self, a,b,e,c,d,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b

    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def setA(self, a):
        self.__a = a
    
    def setB(self, b):
        self.__b = b
    
    def setC(self, c):
        self.__c = c
        
    def setD(self, d):
        self.__d = d

    def setE(self, e):
        self.__e = e

    def setF(self, f):
        self.__f = f
        
    def isSolvable(self):
        if (self.__a * self.__d) != (self.__b * self.__c):
            return True
        else:
            return print("No Solution.")
    
    def getX(self):
        x = ((self.__e * self.__d) - (self.__b * self.__f))/((self.__a * self.__d) - (self.__b * self.__c))
        return x
    
    def getY(self):
        y = ((self.__a * self.__f) - (self.__e * self.__c))/((self.__a * self.__d) - (self.__b * self.__c))
        return y


a1, a2, a3, a4, a5, a6 = eval(input("Enter 6 numbers representing the equation: "))

equation_results = LinearEquation(a1, a2, a3, a4, a5, a6)

print(equation_results.getX())
print(equation_results.getY())

    
        
        
    
            
            
            
            

