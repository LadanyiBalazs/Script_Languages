#!/usr/bin/env python3

def loop(n, debug=False):
    if(debug == False):
        for n in range(1, n+1):
            print(n, end=" ")
    elif(debug == True):
        print("\n# ciklus kezdete:")
        for n in range(1, n+1):
            print(n, end=" ")
        print("\n# ciklus vége")
 
 
def main():
    """
    Returns different outputs for different default arguments.
    """
    loop(5)
    loop(5, debug=True)
 
 
if __name__ == "__main__":
    main()