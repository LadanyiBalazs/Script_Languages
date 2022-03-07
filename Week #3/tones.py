#!/usr/bin/env python3
 
MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"
 
 
def deepOrHigh(word):
    w = list(word)
    a = 0
    b = 0
    for c in w:
        if(MELY_MGHK.find(c) != -1):
            a += 1
        if(MAGAS_MGHK.find(c) != -1):
            b += 1
    if(a > 0 and b > 0):
        print(word + " -> vegyes")
    elif(a > 0 and b == 0):
        print(word + " -> mély")
    elif(a == 0 and b != 0):
        print(word + " -> magas")
    else:
        print(word + " -> semmilyen")

 
def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    for word in words:
        deepOrHigh(word)
 
 
if __name__ == "__main__":
    main()