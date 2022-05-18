# Daily Coding Problem [Medium]
# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than linear time. 
# If the element doesn't exist in the array, return null.
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
# You can assume all the integers in the array are unique.


def find_index(arr, element):
    # binary search
    low, high = 0, len(arr)

    while low < high:
        mid = low + (high-low) // 2 
        
        if element == arr[mid]:
            return mid
        if arr[low] <= arr[mid]:
            if element >= arr[low] and element < arr[mid]:
                high = mid
            else:
                low = mid + 1
        else:
            if element <= arr[high-1] and element > arr[mid]:
                low = mid + 1
            else:
                high = mid
            
    return None

if __name__ == "__main__":
    arr = [13, 18, 25, 2, 8, 10]
    element = 8
    result = find_index(arr, element)
    print(result)


# Example
# [13, 18, 25, 2, 8, 10] 
# element 8
# return 4

# Time complexity
# O(logn)