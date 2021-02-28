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
        x = eval(input("Enter the amount the be withdrawn: "))
        self.__balance -= x
        return 
    
    def deposit(self):
        x = eval(input("Enter the amount the be deposit: "))
        self.__balance += x
        return 
    
    def getID(self):
        return self.__ID
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
my_acc_0 = Account(0, 100, 0.045)
my_acc_1 = Account(1, 100, 0.045)
my_acc_2 = Account(2, 100, 0.045)
my_acc_3 = Account(3, 100, 0.045)
my_acc_4 = Account(4, 100, 0.045)
my_acc_5 = Account(5, 100, 0.045)
my_acc_6 = Account(6, 100, 0.045)
my_acc_7 = Account(7, 100, 0.045)
my_acc_8 = Account(8, 100, 0.045)
my_acc_9 = Account(9, 100, 0.045)

account_list = [my_acc_0,my_acc_1,my_acc_2,my_acc_3,my_acc_4,my_acc_5,\
                my_acc_6,my_acc_7,my_acc_8,my_acc_9]
#my_acc.deposit()
#print(my_acc.getBalance())
#print(my_acc.getID())


def atm():
    account_id = eval(input("Enter an account id: "))
    while account_id not in [0,1,2,3,4,5,6,7,8,9]:
        atm()
    else:
        while True:
            button = eval(input("Main Menu: \n 1:Check Balance \n 2:Withdraw \n 3:Deposit \n 4:Exit\n"))
            if button == 1:
                print("Account Balance: " + str(account_list[account_id].getBalance()))
            if button == 2:
                account_list[account_id].withdraw()
            if button == 3:
                account_list[account_id].deposit()
            if button == 4:
                atm()
            
                
atm()









