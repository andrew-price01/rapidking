#!/usr/bin/env python3
import sys

digitList = ('00011', '00101', '00110', '01001', '01010', '01100', '10001', '10010', '10100', '11000')

def getDigit(d):
    if d == '0':
        print(11000)

    for i in digitList:
        bar1 = int(i[0]) * 7
        bar2 = int(i[1]) * 4
        bar3 = int(i[2]) * 2
        bar4 = int(i[3]) * 1
        bar5 = int(i[4]) * 0
        digit = bar1 + bar2 + bar3 + bar4 + bar5
        if digit == int(d):
            print(i)

def getInput():
    zipcode = input("Enter a zipcode: ")
    for num in zipcode:
        getDigit(num)

'''def printDigit(d):

def printBarCode(zipCode):'''

def main():
    getInput()

if __name__ == '__main__':
    main()

    exit(0)
