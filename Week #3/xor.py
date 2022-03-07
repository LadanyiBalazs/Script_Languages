#!/usr/bin/env python3

a = "python"
b = None

def main():
    if bool(a) == True or bool(b) == True:   
        if bool(a) == True and bool(b) == True:
            print(False)
        else:
            print(True)
    else:
        print(False)
    return 


if __name__ == "__main__":
    main()