#!/usr/bin/env python3

from unittest import result


inp = [1, 0, 1, 1, 0, 1, 0, 0]


def main():
    #1 result = [s.lower() for s in inp]

    #2 result = [s.capitalize() for s in inp]
    
    #3 result = [0 for n in range(10)]

    #4 result = [n for n in inp if n % 2 == 0]
    
    #5 inp = [str(n) for n in range(1,11)]
    #5 result = [int(s) for s in inp]

    #6 result = [int(c) for c in inp]

    #7 result = [len(s) for s in inp.split()]

    #8 result = [s[0] for s in inp.split()]

    #9 result = [(s, len(s)) for s in inp.split()]

    #10 result = [n for n in range(10) if n % 2 == 0]

    #11 result = [(n * n) for n in range(20) if (n * n) % 2 == 0]

    #12 result = [(n * n) for n in range(20) if (n * n) % 10 == 4]
    
    #13 inp = [chr(x) for x in range(65, 91)]
    #13 result = "".join([c for c in inp])

    #14 result = [s.strip() for s in inp]

    #15 result = "".join([str(n) for n in inp])
    return print(result)
    
if __name__ == "__main__":
    main()