#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:32:59 2021

@author: furkanoruc
"""


class Account:
    def __init__ (self, ID = int(0), balance = float(100.0), annualInterestRate = 0.0):
        self.__ID = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def setID(self, ID):
        self.__ID = ID
    def setBalance(self, balance):
        self.__balance = balance
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    
    def withdraw(self):
        x = input("Enter the amount the be withdrawn: ")
        self.__balance += x
        return self.__balance
    
    def deposit(self):
        x = eval(input("Enter the amount the be deposit: "))
        return print("Total Balance with Deposit:"  + str(self.__balance + x))
    
    def getID(self):
        return self.__ID
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
my_acc = Account(1122,20000, 0.045)

my_acc.deposit()
#print(my_acc.getBalance())
print(my_acc.getID())












