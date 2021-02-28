#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random
import turtle
import math

x1, y1, radius_1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))

x2, y2, radius_2 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))



turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(radius_1) # Draw a circle

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.circle(radius_2) # Draw a circle
if math.sqrt((x1-x2)**2 + (y1-y2)**2) < abs(radius_1 - radius_2):
    
    turtle.write("circle2 is inside circle1")
    
else:
    
    turtle.write("circle2 is inside circle1")

    