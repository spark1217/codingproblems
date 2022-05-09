# Daily Coding Problem [Easy]
# Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
# For example, for the input [1, 2, 3, 10], you should return 7.
# Do this in O(N) time.

def find_smallest_int(arr):
    if min(arr) > 1:
        return 1
    possiblemin = 1
    # arr.sort()                  # O(nlogn)
    for i in arr:
        if i <= possiblemin:
            possiblemin = possiblemin + i
        else:
            return possiblemin
    


if __name__ == "__main__":
    arr = [1,2,5]
    result = find_smallest_int(arr)
    print(result)


# Example
# [1, 2, 3, 10] --> 7
# [1, 2, 5] --> 4

# Time complexity
# O(n)
# O(nlogn) if a given array is not sorted

