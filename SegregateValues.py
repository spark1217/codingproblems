# Daily Coding Problem [Hard]
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array 
# so that all the Rs come first, the Gs come second, and the Bs come last. 
# You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


def segregate_values(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    # R : arr[0:dict['R']]
    # G : arr[dict['R']:dict['R']+dict['G']]
    # B : arr[dict['R']+dict['G']]:]
    for i in range(len(arr)):
        if arr[i] != 'R' and i < dict['R']:
            arr[i] = 'R'
        elif arr[i] != 'G' and (i >= dict['R'] and i < dict['R']+dict['G']):
            arr[i] = 'G'
        elif arr[i] != 'B' and (i >= dict['R']+dict['G'] and i < len(arr)):
            arr[i] = 'B'

    return arr


if __name__ == "__main__":
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    result = segregate_values(arr)
    print(result)



# Example
# ['G', 'B', 'R', 'R', 'B', 'R', 'G'] --> ['R', 'R', 'R', 'G', 'G', 'B', 'B']


# Time complexity
# O(n)