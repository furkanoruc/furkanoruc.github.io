#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 04:35:00 2021

@author: furkanoruc
"""


years = 5
b = 7
d = 13
i = 45
year = 365
day = 24
hour = 60
minute = 60

current_population = 312032486

yearly_birth = (year*day*hour*minute) // (b)
left_yearly_birth = (year*day*hour*minute) % (b)
yearly_death = (year*day*hour*minute) // (d)
left_yearly_death = (year*day*hour*minute) % (d)
yearly_immigrant = (year*day*hour*minute) // (i)
left_yearly_immigrant = (year*day*hour*minute) % (i)



population = []
for k in range(1,years+1):
    yearly_birth = k*(year*day*hour*minute) // (b)
    yearly_death = k*(year*day*hour*minute) // (d)
    yearly_immigrant = k*(year*day*hour*minute) // (i)
    population.append(current_population + (yearly_birth - yearly_death + yearly_immigrant))
    print (population[k-1])
