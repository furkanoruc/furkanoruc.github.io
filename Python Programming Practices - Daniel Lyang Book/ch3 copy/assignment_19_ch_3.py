#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import turtle

x1, y1 = eval(input("Enter x1 and y1 for point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

distance=((x1-x2)**2+(y1-y2)**2)**0.5

turtle.penup()
turtle.goto(x1, y1) # Move to (x1, y1)
turtle.pendown()
turtle.write(str( x1) + str(",") + str( y1), font=("Arial",14, "normal"))
turtle.goto(x2, y2) # Draw a line to (x2, y2)
turtle.write(str( x2) + str(",") + str( y2), font=("Arial",14, "normal"))

turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance, font=("Arial",14, "normal"))

turtle.done()
