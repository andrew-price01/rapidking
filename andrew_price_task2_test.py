#!/usr/bin/env python3
import sys
import andrew_price_task2_hw7
import urllib.request

def getInput():
    """
    Pulls barCodeData.txt from url,
    loop through each line and put into a list,
    Calls printZipCode from andrew_price_task2_hw7.py and passes in each
    object in list.
    """
    L = []
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    response = urllib.request.urlopen(url).read().decode("utf-8")
    for word in response.splitlines():
        L.append(word)
    for i in L:
        print("Enter a zip code: ", i)
        andrew_price_task2_hw7.printZipCode(i)

def main():
    """
    Calls getInput()
    """
    getInput()

if __name__ == '__main__':
    main()

    exit(0)
