#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import math

radius = 6371000 #in meters

atlanta = [33.72, -84.52]
savannah = [32, -81.21]
orlando = [28.54, -81.38]
charlotte = [35.22, -80.84]

a1 = math.radians(33.72)
a2 = math.radians(-84.52)
a3 = math.radians(32)
a4 = math.radians(-81.21)
a5 = math.radians(28.54)
a6 = math.radians(-81.38)
a7 = math.radians(35.22)
a8 = math.radians(-80.84)

atlanta = [a1, a2]
savannah = [a3, a4]
orlando = [a5, a6]
charlotte = [a7, a8]

def dist(x1, x2, y1, y2, radius):
    distance = radius* math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1) * math.cos(x2) * math.cos(y1-y2))
    return distance


#all distances in meters
atlanta_charlotte = dist(atlanta[0], charlotte[0], atlanta[1], charlotte[1], radius)
atlanta_orlando = dist(atlanta[0], orlando[0], atlanta[1], orlando[1], radius)
atlanta_savannah = dist(savannah[0], atlanta[0], savannah[1], atlanta[1], radius)
orlando_savannah = dist(savannah[0], orlando[0], savannah[1], orlando[1], radius)
orlando_charlotte = dist(charlotte[0], orlando[0], charlotte[1], orlando[1], radius)
savannah_charlotte = dist(charlotte[0], savannah[0], charlotte[1], savannah[1], radius)


def area(s1,s2,s3):
    
    s = (s1 + s2 + s3)/2

    area_square = (s*(s-s1)*(s-s2)*(s-s3))

    area = area_square**(0.5)
    return area

total_area = area(atlanta_charlotte, atlanta_savannah, savannah_charlotte) + area(atlanta_orlando, atlanta_savannah, orlando_savannah)

km_area = total_area/1000000

print("The area of the 2 triangle is (km^2): " + str(km_area))
print("The area of the 2 triangle is (m^2): " + str(total_area))





