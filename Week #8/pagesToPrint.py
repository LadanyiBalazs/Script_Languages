#!/usr/bin/env python3

import sys

def main():
    li : list[int] = []
    x : str = input("What pages would you like to print? ")
    for n in x.split(","):
        if n.find("-") == -1:
            li.append(int(n))
        else:
            a : int = int(n[:n.find("-")])
            b : int = int(n[n.find("-")+1:])
            for nn in range(a,b+1):
                li.append(nn)
    print(li)

    
if __name__ == "__main__":
    main()