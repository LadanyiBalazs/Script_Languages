#!/usr/bin/env python3

def main():
    print("Type a number: ")
    s = input()
    s = str(s)
    return print(s[::-1])

if __name__ == "__main__":
    main()