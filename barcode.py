#!/usr/bin/env python3
import sys

digitList = ('00011', '00101', '00110', '01001', '01010', '01100', '10001', '10010', '10100')


def getDigit(d):
    for i in digitList:
        bar1 = int(i[0]) * 7
        bar2 = int(i[1]) * 4
        bar3 = int(i[2]) * 2
        bar4 = int(i[3]) * 1
        bar5 = int(i[4]) * 0
        digit = bar1 + bar2 + bar3 + bar4 + bar5
        if digit == int(d):
            printBarCode(i)

def checkDigit(zipcode):
    checkDigit = 0
    multOfTen = 10
    for i in zipcode:
        checkDigit += int(i)
    while multOfTen < 50:
        if checkDigit < multOfTen:
            check = multOfTen - checkDigit
            getDigit(check)
            break
        else:
            multOfTen += 10


def getInput():
    zipcode = input("Enter a zipcode: ")
    sys.stdout.write("|")
    for num in zipcode:
        if num != '0':
            getDigit(num)
        else:
            sys.stdout.write("||:::")
    checkDigit(zipcode)
    sys.stdout.write("|")
    print('\n')

'''def printDigit(d):'''

def printBarCode(bar):
    for p in bar:
        if p == "0":
            sys.stdout.write(":")
        elif p == "1":
            sys.stdout.write("|")
    


def main():
    getInput()

if __name__ == '__main__':
    main()

    exit(0)
