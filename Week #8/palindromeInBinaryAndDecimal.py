#!/usr/bin/env python3

import pygyak as pgy

def main():
    x : int = 0
    for n in range(1_000_000):
        if n == 0:
            pass
        elif pgy.is_palindrome(n) and pgy.is_palindrome(bin(n)[2:]):
            x += n
    print(x)
    
if __name__ == "__main__":
    main()