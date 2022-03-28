#!/usr/bin/env python3

OPEN = ["[", "{", "("]
CLOSE = ["]", "}", ")"]

def test(text):
    stack = []
    for char in text:
        if char in OPEN:
            stack.append(char)
        elif char in CLOSE:
            index = CLOSE.index(char)
            if((len(stack) > 0) and (OPEN[index] == stack[-1])):
                stack.pop()
            else:
                return False
    if(len(stack) == 0):
        return True
    else:
        return False

def main():
    print("((5+3)*2+1): ", test("((5+3)*2+1)"))
    print("{[(3+1)+2]+}: ", test("{[(3+1)+2]+}"))
    print("(3+{1-1)}: ", test("(3+{1-1)}"))
    print("[1+1]+(2*2)-{3/3}: ", test("[1+1]+(2*2)-{3/3}"))
    print("(({[(((1)-2)+3)-3]/3}-3): ", test("(({[(((1)-2)+3)-3]/3}-3)"))

if __name__ == "__main__":
    main()