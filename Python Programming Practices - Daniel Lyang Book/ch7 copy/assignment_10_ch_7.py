#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import math
import time
import datetime
now = datetime.datetime.now()


class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second


    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second
    
    def setHour(self, hour):
        self.__hour = hour
    
    def setMinute(self, minute):
        self.__minute = minute
    
    def setSecond(self, second):
        self.__second = second
        
        
    def setTime(self, elapseTime):
        minutes = elapseTime // 60
        left_seconds = elapseTime % 60
        hours = minutes // 60
        left_minutes = minutes % 60
        return hours, left_minutes, left_seconds


x =  time.time()

x1 = now.hour
x2 = now.minute
x3 = now.second

timer = Time(x1, x2, x3)
print("The Exact Time (Dependent on the Computer: " + str(timer.getHour()) + ": "+ str(timer.getMinute()) + ": "+ str(timer.getSecond()))
print("The Elapsed Time is: " + str(x))
print("The Elapsed Time in Hours,Mins and Secs (Dependent on the Computer: " + str(timer.setTime(x)))

#print()

#print(equation_results.getX())


    
        
        
    
            
            
            
            

