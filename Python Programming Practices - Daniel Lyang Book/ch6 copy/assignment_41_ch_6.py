#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import turtle
import math
import random

def drawPoint():
  for i in range (0,20):
    x = random.randint(1,100)
    y = random.randint(1,100)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()


def drawCircle(x = 0, y = 0, radius = 150): #rearrange required for 50
  turtle.penup()
  turtle.goto(x, y-radius)
  turtle.pendown()
  turtle.circle(radius)

def drawRectangle(x = 0, y = 0, width = 300, height = 300): #rearrange for 30, 30
  turtle.penup() # Pull the pen up
  turtle.goto(x + width / 2, y + height / 2)
  turtle.pendown() # Pull the pen down
  turtle.right(90)
  turtle.forward(height)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(height)
  turtle.right(90)
  turtle.forward(width)

drawRectangle()

drawCircle()

drawPoint()




