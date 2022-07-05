# Suppose you're given an array of varying length containing multiple #s, and a number x. 
# Using these inputs, write a short program in Python find the remainder of the array multiplication divided by x.
# For example,
# Given the following array and x,
# [5,2,4,1,5]
# x = 6
# ouput should be
# (5*2*4*1*5)%6 = 2


import numpy as np
import math
def mul_div(arr, x):
    # nparr = np.array(arr)
    # mul = np.prod(arr)
    return math.prod(arr) % x


array = [5,2,4,1,5]
x = 6
res = mul_div(array, x)
print(res)

