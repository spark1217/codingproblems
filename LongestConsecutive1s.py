# Daily Coding Problem [Easy]
# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
# For example, given 156, you should return 3.

def longest_consecutive_1s(n):
    binary_n = bin(n)
    max_1 = 0
    temp = 0
    str_bin_n = str(binary_n)[2:]
    for i in range(len(str_bin_n)):
        if str_bin_n[i] == '1':
            temp += 1
        elif str_bin_n[i] == '0':
            max_1 = max(max_1, temp)
            temp = 0
    return max_1


if __name__ == "__main__":
    n = 156
    result = longest_consecutive_1s(n)
    print(result)



# Example
# n = 156 --> return 3
# n = 51 --> return 2

# Time complexity
# O(n)