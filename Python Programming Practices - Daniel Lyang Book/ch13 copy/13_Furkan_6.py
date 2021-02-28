#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""
import urllib.request

#http://www.abrahamlincolnonline.org/lincoln/speeches/gettysburg.htm
#Taken from Bliss Copy

#the_file = open("lincoln.txt", "w")
#the_file = open("lincoln.txt", "r")

url = "http://www.abrahamlincolnonline.org/lincoln/speeches/gettysburg.htm"
url= url.strip()
infile = urllib.request.urlopen(url)
the_file = infile.read().decode()


count = 0
for line in the_file:
    for word in line.strip():
        count += 1

print("Lincoln Text Count: " + str(count))

#The number does not match the exact lincoln number since original website
#does not work and this website includes several versions, together.