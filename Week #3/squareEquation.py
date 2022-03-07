#!/usr/bin/env python3


def main():
    sum = 0
    sum2 = 0
    nums = range(1, 101)
    for i in nums: 
        sum += int(pow(i, 2))
        sum2 += int(i)
    sum2 = pow(sum2, 2)
    return print(sum2 - sum)
    

if __name__ == "__main__":
    main()