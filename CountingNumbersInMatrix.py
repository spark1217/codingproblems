# Daily Coding Problem [Hard]
# Let A be an N by M matrix in which every row and every column is sorted.
# Given i1, j1, i2, and j2, compute the number of elements of A smaller than A[i1, j1] and larger than A[i2, j2].
# For example, given the following matrix:
# [[1, 3, 7, 10, 15, 20],
# [2, 6, 9, 14, 22, 25],
# [3, 8, 10, 15, 25, 30],
# [10, 11, 12, 23, 30, 35],
# [20, 25, 30, 35, 40, 45]]
# And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 14 as there are 14 numbers in the matrix smaller than 6 or greater than 23.

def count_nums_matrix(matrix, i1, j1, i2, j2):
    small = matrix[i1][j1]
    large = matrix[i2][j2]
    count = 0
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[n][m] < small or matrix[n][m] > large:
                count += 1

    return count



if __name__ == "__main__":
    matrix = [[1, 3, 7, 10, 15, 20], [2, 6, 9, 14, 22, 25], [3, 8, 10, 15, 25, 30], [10, 11, 12, 23, 30, 35], [20, 25, 30, 35, 40, 45]]
    i1 = 1
    j1 = 1
    i2 = 3
    j2 = 3
    result = count_nums_matrix(matrix, i1, j1, i2, j2)
    print(result)


# Example
# matrix = [[1,2,3],[2,4,6],[3,4,10]]
# i1=0, j1=1, i2=1, j2=2
# return 2

# Time complexity
# O(n^2)