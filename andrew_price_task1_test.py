#!/usr/bin/env python3
import sys
import re
import urllib.request
import minivan

header = []

def getInput():
    """
    Description: Get test data from given url. Loop through each line, remove white space and commas,
    add to header list. 
    """
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    response = urllib.request.urlopen(url).read().decode("utf-8")
    for line in response.splitlines():
        line = line.replace(',', '')
        line = line.replace(' ', '')
        header.append(line)
    header.remove(header[0])

def testCheckDoors():
    """
    Description: Get each bool and char and call main script function
    """
    x = 1
    for i in header:
        ld = i[2]
        rd = i[3]
        cl = i[4]
        ml = i[5]
        li = i[6]
        lo = i[7]
        ri = i[8]
        ro = i[9]
        gs = i[10]
        print("Reading Record {}:".format(x))
        print("Left dashboard switch (0 or 1): {}".format(ld))
        print("Right dashboard switch (0 or 1): {}".format(rd))
        print("Child lock switch (0 or 1): {}".format(cl))
        print("Master unlock switch (0 or 1): {}".format(ml))
        print("Left inside handle (0 or 1): {}".format(li))
        print("Left outside handle (0 or 1): {}".format(lo))
        print("Right inside handle (0 or 1): {}".format(ri))
        print("Right ouside handle (0 or 1): {}".format(ro))
        print("Gear shift position (P, N, D, 1, 2, 3, Or R): {}".format(gs))
        minivan.checkDoors(ld, rd, cl, ml, li, lo, ri, ro, gs)
        print("\n")
        x+=1

def main():
    """
    Call getInput() and testCheckDoors()
    """
    getInput()
    testCheckDoors()
    
    

if __name__ == '__main__':
    main()
    
    exit(0)
