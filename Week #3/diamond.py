#!/usr/bin/env python3

n = int(input("Type an odd number:"))
def main():
    if n%2 == 0:
        print("This is not an odd number.")
    else:
        g = round(n/2 + 0.1)
        for i in range(g):            
            x = "*" * (2*i + 1)
            print(x.center(n))
        for i in range(g - 2, -1, -1):
            x = "*" * (2*i + 1)
            print(x.center(n))
    return 


if __name__ == "__main__":
    main()