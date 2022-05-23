# Daily Coding Problem [Easy]
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

def perfect_num(n):
    if n < 1:
        return -1
    count = 0
    integer = 0
    while count < n:
        integer += 1
        temp = integer
        is_perfect = 0
        while temp > 0:
            is_perfect += temp % 10
            temp = temp // 10
        is_perfect += temp % 10

        if is_perfect == 10:
            count += 1
    return integer


if __name__=="__main__":
    n = 15
    result = perfect_num(n)
    print(result)


# Example
# n = 1 --> return 19
# n = 2 --> return 28
# n = 15 --> return 154

# Time complexity
# O(n^2)