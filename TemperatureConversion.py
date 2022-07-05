# Write a python function to convert temperatures from fahrenheit to celsius. 
# More specifically, your function should be able to read in a list of unspecified length and print out the celsius temperature for each item.
# The formula to convert from fahrenheit to celsius is:
# (fahrenheit temperature - 32) * 5/9


def temp_conversion(arr):
    celsius = []
    for i in arr:
        celsius.append("%.2f" % ((i-32)*5/9))
    return celsius



arr = [80, 27, 64, 102, 59]
res = temp_conversion(arr)
print("fahrenheit: ", arr, '\ncelsius: ', res)