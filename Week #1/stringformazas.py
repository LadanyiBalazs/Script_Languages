#!/usr/bin/env python3

def main():
    nev = input("What is your name? ")
    szin = input("What is your favorite color? ")
    nev = nev.strip()
    szin = szin.strip()
    szin = szin.lower()
    if szin == "blue":
        print("Hello " + nev + "!\n" + "Blue calls to mind feelings of calmness or serenity.")
    elif szin == "yellow":
        print("Hello " + nev + "!\n" + "You have a happy disposition and are cheerful and fun to be with.")
    elif szin == "green":
        print("Hello " + nev + "!\n" + "Lovers of green are often said to be loyal, honest, and affectionate.")
    elif szin == "red":
        print("Hello " + nev + "!\n" + "You exude a powerful energy and upon entering a room, your arrival is immediately known.")
    else:
        print("Pick a different color")

if __name__ == "__main__":
    main()