# Daily Coding Problem [Easy]
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def addup_to_k(arr, k):
    for i in arr:
        temp = k - i
        if temp in arr:
            return True
    return False


if __name__ == "__main__":
    arr = [23, 5, 3, 1]
    k = 8
    result = addup_to_k(arr, k)
    print(result)


# Example
# input = [10, 15, 3, 7]
# k = 17
# return True

# input = [23, 5, 3, 1]
# k = 8
# return True


# Time complexity
# O(n)