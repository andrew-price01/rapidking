#!/usr/bin/env python3

#This module was codded by Burak Deniz for team Rapid King

import sys, os


counter = 1

while counter < 100:

    print (" ")

    LD = str(input("Left Dashboard swich (1/0) ?"))
    print ("L.D. Swich = " + LD)
    print (" ")

    RD = str(input("Right Dashboard swich (1/0) ?"))
    print ("R.D. Swich = " + RD)
    print (" ")


    CL = str(input("Child Lock swich (1/0) ?"))
    print ("C.L. Swich = " + CL)
    print (" ")


    ML = str(input("Master Unlock swich (1/0) ?"))
    print ("M.L. Swich = " + ML)
    print (" ")


    LI = str(input("Left Inside swich (1/0) ?"))
    print ("L.I. Swich = " + LI)
    print (" ")


    LO = str(input("Left Outside swich (1/0) ?"))
    print ("L.O. Swich = " + LO)
    print (" ")


    RI = str(input("Right Inside swich (1/0) ?"))
    print ("R.I. Swich = " + RI)
    print (" ")


    RO = str(input("Right Outside swich (1/0) ?"))
    print ("R.O. Swich = " + RO)
    print (" ")


    GS = input("Gear swift Position (P,N,D,1,2,3, or R) ?")
    print ("G.S. Swich = " + GS)
    print (" ")


    if GS == 'R' or GS == 'D' or GS == 'N' or GS == 'r' or GS == 'd' or GS == 'n' or GS == '1' or GS == '2' or GS == '3' :

        print ("BOTH DOORS STAY CLOSED")
        print

    elif ML == '1' and GS == 'P' or GS == 'p' :

        print ("BOTH DOORS OPEN")
        print

    elif ML == '0' and GS == 'P' or GS == 'p' :

        print ("BOTH DOORS CLOSE")
        print

    elif GS != 'R' or GS != 'D' or GS != 'N' or GS != 'r' or GS != 'd' or GS != 'n' or GS != '1' or GS != '2' or GS != '3' :

        print ("INVALID RECORD. BOTH DOORS STAY CLOSED")
        print
    print ("..................................................")
    counter += 1
    print ("Reading record # '",counter,"'(Use Keyboard Interrupt to Stop the Program):")
    print (" ")

exit(0)
