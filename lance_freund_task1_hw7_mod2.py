#!/usr/bin/env python3
# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys
from urllib.request import urlopen
import re
from burak_deniz_task1_hw7_mod1 import control

def fileup():
    """
    This function captures file and decodes the data
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as file:

        for i in file:
            line = i.decode('utf-8')
            #data_clean = (line.split())

            if line[0] is "R":
                line = line.replace(",","" )
                line = line.replace("R1", "")
                perams = line
                print(perams)

fileup()
control()


"""
            LD = perams[1]
            RD = perams[3]
            CL = perams[5]
            ML = perams[7]
            LI = perams[9]
            LO = perams[11]
            RI = perams[13]
            RO = perams[15]
            GS = perams[17]
            print(perams)
        #switchInfo=(LD,RD,CL,ML,LI,LO,RI,RO,GS)
        #print(switchInfo)

"""
def main():
    """
    runs module
    """
    fileup()

if __name__ == '__main__':
    main()

    exit(0)
