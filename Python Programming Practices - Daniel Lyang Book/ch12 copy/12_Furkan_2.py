#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:32:59 2021

@author: furkanoruc
"""

class Location:
    def __init__(self, n_row = int, n_column = int):
        self.__n_row = n_row
        self.__n_column = n_column
        
    def getRow(self):
        return self.__n_row
    def getColumn(self):
        return self.__n_column

    
    def setRow(self, n_row):
        self.__row = n_row
    def setColumn(self, n_column):
        self.__column = n_column

        
    def entry(self):
        matrix = []
        t = self.__n_row
        r = self.__n_column
        for i in range(int(t)):
            matrix.append([])
            for j in range(int(r)):
                matrix[i].append(eval(
                    input("Enter elements of the matrix, row by row: ")))
        return matrix
    
    def location_Largest(self, matrix):
        largest = matrix[0][0]
        t = self.__n_row
        r = self.__n_column
        for i in range(int(t)):
            for j in range(int(r)):
                if matrix[i][j] >= largest:
                    largest = matrix[i][j]
                    i_holder = i
                    j_holder = j
        return "Largest element is " + str(largest) + " with location row: " +\
            str(i_holder) + " and column: " + str(j_holder)

#it could be as well arranged as latest largest and earliest largest.
            
sunday = Location(input("n_row: "), input("n_column: "))


print(sunday.location_Largest(sunday.entry()))





