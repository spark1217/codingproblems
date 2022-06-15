# Given an integer matrix, m, with an odd # dimensions, n x n, (e.g 3 x 3, 5 x 5, etc), 
# find the sum of middle row as well as the middle column.
# For example:                
# Given
# [[1,2,3],
# [4,5,6],
# [7,8,9]]
# Your program would output:
# 'Sum middle row =' 15 #(e.g. 4+5+6)
# 'Sum middle column =' 15 #(e.g. 2+5+8)

import math

def matrix_sum(arr):
    mid_row = math.floor(len(arr)/2)
    mid_col = math.floor(len(arr[0])/2)

    # row_sum
    row_sum = sum(arr[mid_row])
    print('Sum middle row = ', row_sum)

    # col_sum    
    col_sum = 0
    for i in range(len(arr)):
        col_sum += arr[i][mid_col]
    print('Sum middle column = ', col_sum)

    


if __name__=="__main__":
    arr = [[4,5,6,1,2],[9,2,1,6,7],[7,3,8,3,2],[1,4,5,8,4],[3,6,5,0,2]]
    matrix_sum(arr)


# Example
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# row_sum = 4+5+6 = 15
# col_sum = 2+5+8 = 15

# arr = [[4,5,6,1,2],[9,2,1,6,7],[7,3,8,3,2],[1,4,5,8,4],[3,6,5,0,2]]
# row_sum = 23
# col_sum = 25

# Time complexity
# O(n)