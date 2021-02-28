#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

#scissor (0), rock (1), paper (2)


count_c = 0
count_u = 0

while count_c < 3 and count_u < 3:

    number = eval(input("scissor (0), rock (1), paper (2): "))
    lst = ["scissor", "rock", "paper"] 

    computer = random.randint(0,2)
    #if computer == number:
        #print ("Both of you are " + str(lst[number]) + ", Draw!")
    if computer == 0 and number == 2:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", Computer wins!")
        count_c = count_c + 1
    if computer == 1 and number == 0:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", Computer wins!")
        count_c = count_c + 1
    if computer == 1 and number == 2:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", You win!")
        count_u = count_u + 1
    if computer == 2 and number == 0:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", You win!")
        count_u = count_u + 1
    if computer == 2 and number == 1:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", Computer wins!")
        count_c = count_c + 1
    if computer == 0 and number == 1:
        #print ("Computer is " + str(lst[computer]) + ", You are " + str(lst[number]) + ", You win!")
        count_u = count_u + 1
    
    if count_c == 2:
        print("Computer wins")
        break
    if count_u == 2:
        print("User wins")
        break
    
