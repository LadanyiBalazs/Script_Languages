#!/usr/bin/env python3

p = "192.20.246.138:\n 6666"

def main():
    x = p
    x = p.replace("\n", "")
    x = x.replace(" ", "")
    x = x.replace("\t", "")
    return print(x)
    
if __name__ == "__main__":
    main()