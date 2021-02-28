#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""


word = input("Enter the string: ")

def countLetters(s):
    count = 0
    for i in range (len(s)):
        k = s[i]
        if ord("a") <= ord(str(k)) <= ord("z") or ord("A") <= ord(str(k)) <= ord("Z"):
            count+=1
    return print(count)

countLetters(word)

