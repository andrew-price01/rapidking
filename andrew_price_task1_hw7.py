#!/usr/bin/env python3

def getInput():
    """
    Grabs user input using global variables
    """
    global LD, RD, CL, ML, LI, LO, RI, RO, GS
    LD = input("Left dashboard switch (0 or 1):")
    RD = input("Right dashboard switch (0 or 1):")
    CL = input("Child lock switch (0 or 1):")
    ML = input("Master unlock switch (0 or 1):")
    LI = input("Left inside handle (0 or 1):")
    LO = input("Left outside handle (0 or 1):")
    RI = input("Right inside handle (0 or 1):")
    RO = input("Right outside handle (0 or 1):")
    GS = input("Gear shift position (P, N, D, 1, 2, 3 or R):")

def checkDoors(ld, rd, cl, ml, li, lo, ri, ro, gs):
    """
    Description: Compares and checks for each possible door combination. Prints outcome.
    Arguments: 8 Bool and 1 char
    """
    if ml == '1':
        if gs == 'P':
            if cl == '1':
                if ld == '1' or lo == '1':
                    if rd == '1' or ro == '1':
                        print("Both doors open.")
                    elif rd == '0':
                        if ro == '0':
                            print("Left door open.")
                elif ld == '0':
                    if lo == '0':
                        if rd == '1' or ro == '1':
                            print("Right door open.")
                elif ld == '0' and lo == '0':
                    if rd == '0' and ro == '0':
                        print("Both doors stay closed.")
            elif cl == '0':
                if ld == '1' or li == '1' or lo == '1':
                    if rd == '1' or ri == '1' or ro == '1':
                        print("Both doors open.")
                    elif rd == '0':
                        if ri == '0':
                            if ro == '0':
                                print("Left door open.")
                elif ld == '0':
                    if li == '0':
                        if lo == '0':
                            if rd == '1' or ri == '1' or ro == '1':
                                print("Right door open.")
                elif ld == '0' and li == '0' and lo == '0':
                    if rd == '0' and ri == '0' and ro == '0':
                        print("Both doors stay closed.")
        elif gs == 'N' or gs == 'D' or gs == '1' or gs == '2' or gs == '3' or gs == 'R':
            print("Both doors stay closed.")
        else:
            print("Invalid Record: Both doors stay closed.")
    else:
        print("Both doors stay closed.")


def main():
    """
    Calls getInput() and checkDoors()
    """
    getInput()
    checkDoors(LD, RD, CL, ML, LI, LO, RI, RO, GS)

if __name__ == '__main__':
    main()

    exit(0)

