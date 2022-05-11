# Daily Coding Problem [Easy]
# In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
# Here is an example:
# 1 2 3 4 8
# 5 1 2 3 4
# 4 5 1 2 3
# 7 4 5 1 2
# Write a program to determine whether a given input is a Toeplitz matrix.


def toeplitz(matrix):
    # base case
    if not matrix:
        return True
        
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
 
    return True

if __name__ == "__main__":
    matrix = [[1,2,3,4,8], [5,1,2,3,4], [4,5,1,2,3],[7,4,5,1,2]]
    result = toeplitz(matrix)
    print(result)


# Time complexity
# O(n^2)