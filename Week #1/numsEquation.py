#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        return print("Give 2 arguments!")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        sum = x + y
    return print("The addition is:",sum)

def main2():
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    sum2 = a + b
    print("The addition is:", sum2)

if __name__ == "__main__":
    main()
    main2()