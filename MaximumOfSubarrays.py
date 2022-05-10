# Daily Coding Problem [Hard]
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. 
# You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.


def max_of_subarray(arr, k):
    result = []
    for i in range(len(arr)-k+1):
        result.append(max(arr[i:i+k]))
    return result


if __name__ == "__main__":
    arr = [10, 5, 2, 7, 8, 7]
    k = 4
    result = max_of_subarray(arr, k)
    print(result)



# Example
# arr = [1,2,3,1,4,5,2,3,6], k = 3
# subarray1 = [1,2,3], max = 3
# subarray2 = [2,3,1], max = 3
# subarray3 = [3,1,4], max = 4
# subarray4 = [1,4,5], max = 5
# subarray5 = [4,5,2], max = 5
# subarray6 = [5,2,3], max = 5
# subarray7 = [2,3,6], max = 6
# result = [3,3,4,5,5,5,6]

# arr = [10, 5, 2, 7, 8, 7]
# subarray1 = [10, 5, 2, 7], max = 10
# subarray2 = [5, 2, 7, 8], max = 8
# subarray3 = [2, 7, 8, 7], max = 8
# result = [10, 8, 8]

# Time complexity
# O(n)