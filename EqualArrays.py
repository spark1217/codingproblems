# Given two arrays, write a function in vanilla Python (e.g., no libraries) to check whether or not the arrays are equal. 
# You can consider the two arrays equal if both of them contain the same set of elements - the order of elements can differ.

def equal_arrays(arr1, arr2):
    dict1 = {}
    if len(arr1) != len(arr2):
        return False
    for i in arr1:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1
    for j in arr2:
        if j not in dict1.keys():
            return False
        elif dict1[j] == 0:
            return False
        else:
            dict1[j] -= 1
    
    return True



arr1 = [1,5,6,7,8,0]
arr2 = [0,5,7,8,1,6]
result = equal_arrays(arr1, arr2)
print(result)


# Time complexity
# O(n)