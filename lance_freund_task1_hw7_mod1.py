#!/usr/bin/env/python3

# This is template intended for python modules
# Coded By: Lance Freund
# Weber State University
# lancefreund@mail.weber.edu

#---- Write Python source code below this text. Don't forget your  imports ---
import sys
from urllib.request import urlopen

with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as file:

    switches=[]
    for i in file:
        line = i.decode('utf-8')
        print(line)

exit(0)
