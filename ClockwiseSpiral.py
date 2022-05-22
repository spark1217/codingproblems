# Daily Coding Problem [Easy]
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:
# [[1,  2,  3,  4,  5],
# [6,  7,  8,  9,  10],
# [11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20]]
# You should print out the following:
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def clockwise_spiral(arr):
    visited = []
    columns = len(arr[0])
    rows = len(arr)
    x, y = 0, 0

    # m = row, n = columns, k=x, l=y

    while (x < rows and y < columns):
 
        # Print the first row from the remaining rows
        for i in range(y, columns):
            print(arr[x][i])
 
        x += 1
 
        # Print the last column from the remaining columns
        for i in range(x, rows):
            print(arr[i][columns - 1])
 
        columns -= 1
 
        # Print the last row from the remaining rows
        if (x < rows):
            for i in range(columns - 1, (y - 1), -1):
                print(arr[rows - 1][i])
 
            rows -= 1
 
        # Print the first column from the remaining columns
        if (y < columns):
            for i in range(rows - 1, x - 1, -1):
                print(arr[i][y])
 
            y += 1

    return



if __name__ == "__main__":
    arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
    clockwise_spiral(arr)



# Time complexity
# O(rows*columns)