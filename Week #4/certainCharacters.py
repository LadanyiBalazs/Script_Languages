#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    Prints characters only if in chars.
    """
    return "".join([x for x in list(text) if x in list(chars)])

def main():
    print("-> " + valid("Barking!"))
    print("-> " + valid("KL754", "0123456789"))
    print("-> " + valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()