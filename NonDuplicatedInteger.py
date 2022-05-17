# Daily Coding Problem [Hard]
# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
# find and return the non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
# Do this in O(N) time and O(1) space.

def non_duplicate(arr):
    integers = {}
    for i in arr:
        if i not in integers.keys():
            integers[i] = 1
        else:
            integers[i] += 1
    for j in integers.keys():
        if integers[j] == 1:
            return j
            
if __name__ == "__main__":
    arr = [13,19,13,13]
    result = non_duplicate(arr)
    print(result)


# Example
# [6, 1, 3, 3, 3, 6, 6] --> 1
# [13, 19, 13, 13] --> 19

# Time complexity
# O(n)

# Space complexity
# O(n)