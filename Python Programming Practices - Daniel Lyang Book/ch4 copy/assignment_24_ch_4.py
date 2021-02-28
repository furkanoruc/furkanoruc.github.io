#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

import math

#scissor (0), rock (1), paper (2)

card = eval(input("Pick your card: "))

rank = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

ranker = card % 13

if card <= 13:
    suiter = 0
if card > 13 and card <= 26:
    suiter = 1
if card > 26 and card <= 39:
    suiter = 2
if card > 39 and card <= 52:
    suiter = 3
    
print("The card is " + str(rank[ranker]) + " of " + str(suit[suiter]))
    

