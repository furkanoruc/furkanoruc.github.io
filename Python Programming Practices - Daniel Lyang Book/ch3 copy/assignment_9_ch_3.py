#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:04:33 2021

@author: furkanoruc
"""


#radius of earth

import math

name = (input("Enter Employee Name: "))
hours = eval(input("Enter number of hours worked in a week: "))
pay = eval(input("Enter hourly pay rate: "))
fed_tax = eval(input("Enter federal tax withholding rate: "))
state_tax = eval(input("Enter state tax withholding rate: "))



print("Employee Name: " + str(name))
print("Hours Worked: " + str(hours))
print("Pay Rate: " + str(pay))
print("Gross Pay: " + str(hours*pay))
print("Deductions:")
print("    Federal Withholding: " +str(fed_tax) + str((hours*pay)*fed_tax))
print("    State Withholding: " + str(state_tax) + str((hours*pay)*state_tax))
print("    Total Deduction: " + str((hours*pay)*state_tax + (hours*pay)*fed_tax))
print("    Net Pay: " + str(hours*pay-((hours*pay)*state_tax + (hours*pay)*fed_tax)))






