#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

#filename = input("Enter the filename: ").strip()
f = open("Score",'r')
a = ['morning']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('./test.txt','w')
for line in lst:
    f.write(line)
f.close()



"""
def main():
    k = []
    #filename = input("Enter the filename: ").strip()
    infile = open("Score", "r")
    infile_2 = open("Score", "w")
    filer = readWords(infile)
    for i in range (len(filer.strip())):
        if filer[i:i+7] == "morning":
            k.append(i)
            #i = i + 7
    #infile_2 = open("Score_2", "r") 
    #infile_2 = open("Score_2", "w") 
    i = 0
    while i < (len(filer.strip())):
        if i in k:
            i = i + 7
        infile_2.write(str(filer[i]))
        i += 1
        
    #filer_2 = readWords(infile_2)    
    return
    


def readWords(x):
    s = x.read()
    return s


print(main())
"""















