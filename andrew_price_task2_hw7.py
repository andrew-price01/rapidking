#!/usr/bin/env python3
import sys

digitList = ('00011', '00101', '00110', '01001', '01010', '01100', '10001', '10010', '10100')

'''
Matches digit with digitList values. Calls printBarCode().
'''

def printDigit(d):
    for i in digitList:
        bar1 = int(i[0]) * 7
        bar2 = int(i[1]) * 4
        bar3 = int(i[2]) * 2
        bar4 = int(i[3]) * 1
        bar5 = int(i[4]) * 0
        digit = bar1 + bar2 + bar3 + bar4 + bar5
        if digit == int(d):
            printBarCode(i)

'''
Finds check digit
'''
def checkDigit(zipcode):
    checkDigit = 0
    multOfTen = 10
    for i in zipcode:
        checkDigit += int(i)
    while multOfTen < 50:
        if checkDigit < multOfTen:
            check = multOfTen - checkDigit
            printDigit(check)
            break
        else:
            multOfTen += 10
'''
Checks valid zip code inputs. Calls getDigit() for all numbers not 0. 
If digit is 0, prints barcode. Calls checkDigit()
'''
def getInput():
    zipcode = input("Enter a zipcode: ")
    if len(zipcode) != 5:
        print("Error. Input does not match required length. <95014>")
        getInput()
    elif any(i.isalpha() for i in zipcode):
        print("Error. Only numbers allowed. <95014>")
        getInput()
    else:
        printZipCode(zipcode)

def printZipCode(code):
    sys.stdout.write("|")
    for num in code:
        if num != '0':
            printDigit(num)
        else:
            sys.stdout.write("||:::")
    checkDigit(code)
    sys.stdout.write("|")
    print('\n')

'''
Prints barcode
'''
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
