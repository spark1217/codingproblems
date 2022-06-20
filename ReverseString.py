# Suppose you're given an array of strings, s. Write a function using Python to take each string in the array and reverse it.
# For example:
# Given the following:
# s = ['rac', 'talf', 'tot', 'tob']
# Your function should return:
# s = ['car', 'flat', 'tot', 'bot']


def reverse(arr):
    new = []
    for i in arr:
        new.append("".join(reversed(i)))
    return new


if __name__ == "__main__":
    arr = ['rac', 'talf', 'tot', 'tob']
    result = reverse(arr)
    print(result)


# Time complexity
# O(n)