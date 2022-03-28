#!/usr/bin/env python3

def test(nums):
    nums.sort()
    middle = len(nums) // 2
    median = (nums[middle] + nums[~middle]) / 2
    print(median)

def main():
    test([1, 2, 3, 4, 5])
    test([3, 1, 2, 5, 3])
    test([1, 300, 2, 200, 1])
    test([3, 6, 20, 99, 10, 15])

if __name__ == "__main__":
    main()