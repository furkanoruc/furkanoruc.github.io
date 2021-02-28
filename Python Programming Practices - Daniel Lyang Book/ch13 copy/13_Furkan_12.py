#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""


class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return self.__filled
    
    def setFilled(self, filled):
        self.__filled = filled
        
    def __str__(self):
        return "color " + self.__color + \
            " and filled " + str(self.__filled)

class TriangleError(RuntimeError):
    
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()

    def getSide1(self):
        return self.__side1
    def getSide2(self):
        return self.__side2
    def getSide3(self):
        return self.__side3
    
    
    
class Triangle(GeometricObject):
    def __init__(self,color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self):
        return self.__side1
    def getSide2(self):
        return self.__side2
    def getSide3(self):
        return self.__side3
    
    def setSide1(self, side1):
        self.__side1 = side1
    def setSide2(self, side2):
        self.__side2 = side2
    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3)/2
        return (s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3))**(0.5)
    
    def getPerimeter(self):
        return (self.__side1+self.__side2+self.__side3)
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3)
          


            
            
x1 = eval(input("Side 1 for the Triangle: "))
x2 = eval(input("Side 2 for the Triangle: "))
x3 = eval(input("Side 3 for the Triangle: "))

c = input("Enter the color: ")
f = input("Enter if filled or not (1/0): ")

try:
    tria = Triangle(c, f, x1, x2, x3)
except TriangleError as take:
    print("These three sides", take.getSide1(),  
    take.getSide2(), take.getSide3(), " cannot form a legal triangle.")


print(tria.getArea())
print(tria.getPerimeter())
print(tria.__str__())
print(tria.getColor())
print(tria.isFilled())
    




"""        if self.__side1 + self.__side2 < self.__side3 or \
            self.__side2 + self.__side3 < self.__side1 or self.__side1 \
                + self.__side3 < self.__side2:
            raise RuntimeError("Triangle not Applicable")
            """
        
    
    