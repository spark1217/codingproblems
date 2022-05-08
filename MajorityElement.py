# Daily Coding Problem [Medium]
# Given a list of elements, find the majority element, which appears more than half the time (>floor(len(lst)/2.0))
# You can assume that such element exists.
# For example, given [1,2,1,1,3,4,0], return 1.

import math

def find_majority(arr):
    majority = math.floor(len(arr)/2.0)
    counting = {}
    # counting elements
    for i in range(len(arr)):
        if arr[i] not in counting:
            counting[arr[i]] = 1
        else:
            counting[arr[i]] += 1
    for k in counting:
        if counting[k] == majority:
            return k
        # No majority element exists
        else:
            return -1


if __name__ == "__main__":
    arr = [1,2,1,1,3,4,0]
    result = find_majority(arr)
    print(result)


# Examples
# [1,2,1,1,3,4,0] -> 1
# [1,0,3,1,1,5,4] -> 1
# [3,5,2,6,1,1] -> -1

# Time complexity
# O(n)