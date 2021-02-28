#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import random

import math


lottery = random.randint(100, 999)

guess = eval(input("Enter your lottery pick (three digits): "))

lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery // 10
lotteryDigit3 = lottery % 10


guessDigit1 = guess // 100
guessDigit2 = guess // 10
guessDigit3 = guess % 10

print("The lottery number is", lottery)


if guess == lottery:
    print("Exact match: you won $10,000")

elif(lotteryDigit1 == guessDigit2 and lotteryDigit2 == guessDigit3 and \
     lotteryDigit3 == guessDigit1):
    print("Partial match: you won $3,000")

elif(lotteryDigit1 == guessDigit3 and lotteryDigit3 == guessDigit2 and \
     lotteryDigit2 == guessDigit1):
    print("Partial match: you won $3,000")
    
elif(guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit1 == lotteryDigit3 or \
     guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2 or guessDigit2 == lotteryDigit3 or \
     guessDigit3 == lotteryDigit1 or guessDigit3 == lotteryDigit2 or guessDigit3 == lotteryDigit3):
        print("Partial match: you won $1,000")
        
else:
    print("No win")