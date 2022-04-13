#!/usr/bin/env python3

from fileinput import input

def main():
    sor = [sorted(int(num) for num in line.split()) for line in input()]
    print(sum(num[-1] - num[0] for num in sor))

if __name__ == "__main__":
    main()