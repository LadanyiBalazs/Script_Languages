#!/usr/bin/env python3

num = pow(2, 1000)

def main():
    x = 0
    for n in str(num):
        x += int(n)
    print(x)

if __name__ == "__main__":
    main()