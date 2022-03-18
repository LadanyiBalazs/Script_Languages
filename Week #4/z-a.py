#!/usr/bin/env python3

import sys

def printFromAToZ(a, b):
    """
    Prints the letters of the alphabet between the two endpoints.
    """
    a = ord(a)
    b = ord(b)
    if b < a:
        r = range(a, b-1, -1)
    else:
        r = range(a, b+1)
    for x in r:
        print( chr(x), end="")
    print()

def main():
    args = sys.argv[0].split(".")[0].split("-")
    printFromAToZ(args[0], args[1])

if __name__ == "__main__":
    main()