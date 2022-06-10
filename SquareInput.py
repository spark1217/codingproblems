# Daily Coding Problem [Easy]
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


def square(arr):
    res = []
    for i in arr:
        res.append(i**2)
    res.sort()
    return res


if __name__ == "__main__":
    arr = [-9, -2, 0, 2, 3]
    result = square(arr)
    print(result)



# Time complexity
# O(nlogn)