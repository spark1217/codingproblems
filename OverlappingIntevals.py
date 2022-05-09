# Daily Coding Problem [Easy]
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
# The input list is not necessarily ordered in any way.
# For example, given [[1, 3], [5, 8], [4, 10], [20, 25]], you should return [[1, 3], [4, 10], [20, 25]].

def overlapping_intervals(arr):
    arr.sort()          # O(nlgn)
 
    merged = []
    for i in arr:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
 
    return merged
    


if __name__ == "__main__":
    arr = [[1, 3], [5, 8], [4, 10], [20, 25]]
    result = overlapping_intervals(arr)
    print(result)


# Example
# Input: [(1, 3), (5, 8), (4, 10), (20, 25)]
# Output: [(1, 3), (4, 10), (20, 25)]

# Time complexity
# O(nlogn)
