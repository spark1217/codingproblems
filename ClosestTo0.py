# Suppose you are given a list of Q 1D points. Write code to return the value in Q that is the closest to value j. 
# If two values are equally close to j, return the smaller value. 
# Example:
# Q = [1, -1, -5, 2, 4, -2, 1]
# j = 3
# Output: 2
    

def closest_to_zero(arr, j):
    closest_distance = float("inf")
    value = 0
    for i in arr:
        distance = j - i
        if closest_distance == abs(distance):
            value = min(value, i)

        elif closest_distance > abs(distance):
            value = i
            closest_distance = abs(distance)
        
            
    return  value


arr = [1,-1,-5,2,4,-2,1]
j = 3
result = closest_to_zero(arr, j)
print(result)


# Time complexity
# O(n)