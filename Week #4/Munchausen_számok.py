#!/usr/bin/env python3
# encoding: utf-8


import math

def isMunchausen(number):
    """Megnézi, hogy a megadott szám Munchausen szám-e"""
    return number == sum([math.pow(int(x), int(x)) for x in list(str(number))])

def main():
   # print("2019: ", isMunchausen(2019))
    print("2020: ", isMunchausen(2020))

    for x in range(440000000):
        if (isMunchausen(x)):
            print(x)



if __name__ == "__main__":
    main()