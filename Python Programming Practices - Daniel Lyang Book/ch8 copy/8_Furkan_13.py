#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""



def prefix(s1, s2):
    count = 1
    x = 0
    t = 0
    #w = 0
    if len(s2) > len (s1):
        w = s1
        s1 = s2
        s2 = w
    for i in range (len(s1)):
        if count >= 4:
            break
        else:
            for j in range(0, len(s2)):
                if s1[i] == s2[j]:
                    while t < len(s2)-j:
                        if s1[i+t] == s2[j+t]:
                            t += 1
                            count += 1
                        else:
                            break
                else:
                    break
                    #k = j
                        #while k < len(s2):
                            #if x<=(len(s1)-1) and y<=(len(s2)-1):
                                #if s1[x] == s2[y]:
                                    #count += 1
                                    #x += 1
                                    #y += 1
                            #k += 1
                        
    return i-1, count
            


string1 = input("Enter the 1st string: ")
string2 = input("Enter the 2nd string: ")
index, counter = prefix(string1, string2)

print(string1[index : -(1 + len(string1)-(index+counter))])


#print(string1[(index-counter-1):-(len(string1)-index)])
#print(string1[(6-4+1):(len(string1)-index)])

