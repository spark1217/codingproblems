# Given a matrix of order m*n, find the frequency of even and odd numbers in the matrix.
# For example:
# Given the following inputs
# m = 2, n = 3
# [[ 9, 11, 3 ], 
# [ 4, 12, 2 ]]
# Your function should return the following output:
# Frequency of odd #:  3 (since 9, 11, and 3 are all odd #s)
# Frequency of even #: 3
   
def matrix_frequency(arr):
    count_odd = 0
    total = len(arr[0]) * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] % 2 == 1:
                count_odd += 1

    return  count_odd, total-count_odd


if __name__ == "__main__":
    arr = [[9,11,3],[4,12,2],[5,12,7]]
    odd, even = matrix_frequency(arr)
    print("Frequency of odd #: ", odd)
    print("Frequency of even #: ", even)
    


# Time complexity
# O(mn)