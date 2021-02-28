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


wn = turtle.Screen()

turt = turtle.Turtle()

turt.backward(180)
turt.forward(360)
turt.stamp()
turt.backward(180)
turt.left(90)
turt.forward(100)
turt.stamp()
turt.backward(200)
turt.forward(100)
turt.right(90)
turt.backward(180)

turtle.color("red")
for i in range (-180, 181):
  turt.goto(i, math.sin(math.radians(i)) * 100)
  turt.color("red")
wn.exitonclick()

for i in range (-180, 181):
  turt.goto(i, math.cos(math.radians(i)) * 100)
  turtle.pendown()
  turt.color("blue")
wn.exitonclick()















