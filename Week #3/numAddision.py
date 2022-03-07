#!/usr/bin/env python3


def main():
    a = list(range(100))
    b = str(a).replace(",", "").replace(" ", "").replace("[", "").replace("]", "")
    sum = 0
    for i in b: 
      sum += int(i)
    return print(sum)


if __name__ == "__main__":
    main()