#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random


class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
        
    def getSymbol(self):
        return self.__symbol
    
    def getName(self):
        return self.__name
    
    def setSymbol(self, symbol):
        self.__symbol = symbol
    
    def setName(self, name):
        self.__name = name
    
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setPreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
    
    
    def getChangePercent(self):
        changepercent = ((self.__currentPrice - self.__previousClosingPrice)/self.__currentPrice)*100
        #print(self.changepercent)
        return changepercent


the_symbol = "INTC"
the_name = "Intel Corporation"
the_previous = 20.5
the_current = 20.35

my_class = Stock(the_symbol, the_name, the_previous, the_current)

print(my_class.getChangePercent())











