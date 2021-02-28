#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:14 2021

@author: furkanoruc
"""

#x = "bogazici"
#print(x[2:-4])

binary = input("Enter the Binary Number: ")

#print(binary[4:None])


def binaryToHex(binaryValue):
    bin1 = binaryValue
    base = 0
    dec = 0
    HexValue = ""
    # First convert binary to decimal
    while bin1 > 0:
        remainder = bin1 % 10
        dec = dec + remainder * pow(2, base)
        bin1 = bin1 // 10
        base += 1

    # Then convert decimal to hexadecimal
    while dec != 0:
        temp = dec % 16
        if temp < 10:
            temp = temp + 48
        else:
            temp = temp + 55
        HexValue = chr(temp) + HexValue
        dec = dec // 16
    return HexValue


def main():
    bin1 = eval(input("Enter the binary number: "))
    print("The hexadecimal equivalent of", bin1, "is: ", binaryToHex(bin1))


main()