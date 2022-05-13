# Daily Coding Problem [Hard]
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

import math

def multiply_list(arr):
    res = []
    for i in range(len(arr)):
        arr1 = math.prod(arr[:i])
        arr2 = math.prod(arr[i+1:])
        res.append(arr1*arr2)
    return res


if __name__ == "__main__":
    arr = [3,2,1]
    result = multiply_list(arr)
    print(result)



# Example
# input = [1,2,3,4,5]
# output = [120, 60, 40, 30, 24]

# input = [3,2,1]
# output = [2,3,6]


# Time complexity
# O(n)