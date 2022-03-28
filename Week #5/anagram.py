#!/usr/bin/env python3
s1 ="A gentleman"
s2 ="Elegant man"

TEXT1 = "A gentleman"
TEXT2 = "Elegant asd man"


def anagramTrivial(s1, s2):
    print(sorted("".join(s1.lower().split())) == sorted("".join(s2.lower().split())))        

def anagramDict(TEXT1, TEXT2):
    a = {}
    for w in "".join(TEXT1.lower().split()):
        if w not in a:
            a[w] = 1
        else:
            a[w] += 1
    b = {}
    for w in "".join(TEXT2.lower().split()):
        if w not in b:
            b[w] = 1
        else:
            b[w] += 1
    return print(sorted(a.items()) == sorted(b.items()))

def main():
    anagramTrivial(s1, s2)
    anagramDict(TEXT1, TEXT2)

if __name__ == "__main__":
    main()