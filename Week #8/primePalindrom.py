#!/usr/bin/env python3

import pygyak as pgy

def test(num : int) -> int:
    for n in range(num,num*10):
        if pgy.is_prime(n) and pgy.is_palindrome(n):
            print(n)
            return

def main():
    test(31) == 101
    test(130) == 131
    test(131) == 131
    test(1977) == 10301
        
if __name__ == "__main__":
    main()