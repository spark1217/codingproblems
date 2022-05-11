# Daily Coding Problem [Easy]
# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

import math 

def running_median(arr):
    temp = []
    for i in arr:
        temp.append(i)
        temp.sort()
        temp_len = len(temp)
        if temp_len % 2 == 0:
            median = (temp[math.floor(temp_len/2)-1] + temp[math.floor(temp_len/2)]) / 2
            print(median)
        elif temp_len % 2 == 1:
            median = temp[math.floor(temp_len/2)]
            print(median)
    return

if __name__ == "__main__":
    arr = [2, 1, 5, 7, 2, 0, 5]
    result = running_median(arr)


# Example
# [2, 1, 5, 7, 2, 0, 5]
# [2] --> median 2 
# [2,1] --> median 1.5
# [2,1,5] --> median 2
# [2,1,5,7] --> median 3.5
# [2,1,5,7,2] --> median 2
# [2,1,5,7,2,0] --> median 2
# [2,1,5,7,2,0,5] --> median 2

# Time complexity
# O(n)