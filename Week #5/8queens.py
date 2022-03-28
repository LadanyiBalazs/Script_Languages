#!/usr/bin/env python3

list = [0,4,7,5,2,6,1,3]

def main():
    print("+-----------------+")
    print("|", end = "")
    for n in list:
        if n == 7:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 6:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 5:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 4:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 3:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 2:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 1:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n|", end = "")
    for n in list:
        if n == 0:
            print(" Q", end = "")
        else:
            print(" .", end = "")
    print(" |", end = "")
    print("\n+-----------------+")
    return

if __name__ == "__main__":
    main()