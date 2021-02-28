#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

password = input("Enter the password: ")

def pass_(p):
    count = 0
    counter = 0
    if len(p) >= 8:
        for i in range(len(p)):
            k = p[i]
            if ord("a") <= ord(str(k)) <= ord("z") or ord("A") <= ord(str(k)) <= ord("Z") or ord("0") <= ord(str(k)) <= ord("9"):
                count += 1
                #print(ord(str(k)))
            if ord("0") <= ord(str(k)) <= ord("9"):
                #print(ord("k"))
                counter += 1
        if count == len(p) and counter >= 2:
            return print("Valid Password")
        else:
            return print("Invalid Password")
    else:
        return print("Invalid Password")
    
pass_(password)


#print(ord("5"))
