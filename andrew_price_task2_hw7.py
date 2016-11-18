#!/usr/bin/env python3
import sys

digitList = ('00011', '00101', '00110', '01001', '01010', '01100', '10001', '10010', '10100')

def printDigit(d):
    """
    Matches digit (d) with digitList [] values. Calls printBarCode() with 
    found value.
    """
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
    """
    Finds check digit. Calls printDigit() with check digit
    """
    checkDigit = 0
    multOfTen = 10
    for i in zipcode:
        checkDigit += int(i)
    flag = checkDigit % 2
    while multOfTen < 50:
        if flag == 0:
            sys.stdout.write("||:::")
            break
        elif checkDigit < multOfTen:
            check = multOfTen - checkDigit
            printDigit(check)
            break
        else:
            multOfTen += 10


def getInput():
    """
    Checks valid zip code inputs. Calls printZipCode().
    """
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
    """
    For every digit in zipcode, passes in digit argument to printDigit().
    If digit is 0, prints 0 barcode. Calls checkDigit() last.
    """
    sys.stdout.write("|")
    for num in code:
        if num != '0':
            printDigit(num)
        else:
            sys.stdout.write("||:::")
    checkDigit(code)
    sys.stdout.write("|")
    print('\n')


def printBarCode(bar):
    """
    Prints barcode.
    """
    for p in bar:
        if p == "0":
            sys.stdout.write(":")
        elif p == "1":
            sys.stdout.write("|")
    


def main():
    """
    Calls getInput()
    """
    getInput()

if __name__ == '__main__':
    main()

    exit(0)
