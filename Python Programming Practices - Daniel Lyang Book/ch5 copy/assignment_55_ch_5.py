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



# create screen object 
sc = turtle.Screen() 
   
# create turtle object 
pen = turtle.Turtle() 
   
# method to draw square 
def draw(): 
   
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
   
  pen.forward(30) 
   
  
     
# Driver Code 
if __name__ == "__main__" : 
      
    # set screen 
    sc.setup(600, 600) 
       
    # set turtle object speed 
    pen.speed(100) 
       
    # loops for board 
    for i in range(8): 
       
      # not ready to draw 
      pen.up() 
       
      # set position for every row 
      pen.setpos(0, 30 * i) 
       
      # ready to draw 
      pen.down() 
       
      # row 
      for j in range(8): 
       
        # conditions for alternative color 
        if (i + j)% 2 == 0: 
          col ='black'
       
        else: 
          col ='white'
       
        # fill with given color 
        pen.fillcolor(col) 
       
        # start filling with colour 
        pen.begin_fill() 
       
        # call method 
        draw() 
        # stop filling 
        pen.end_fill() 
       
    # hide the turtle 
    pen.hideturtle() 
       
    # This code is contributed by Deepanshu Rustagi. 


















