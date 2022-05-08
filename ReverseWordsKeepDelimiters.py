# Daily Coding Problem [Hard]
# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters
# For example, given "hello/world:here", return "here/world:hello"
# Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

def ReverseWordsKeepDelimiters(s):
    arr1 = []
    temp = []
    # transform a given string to an array
    for i in range(len(s)):
        if s[i] == '/':
            # append a word to arr1 if a character is a delimiter
            word = ''.join(temp)
            arr1.append(word)
            temp = []
            arr1.append('/')
        elif s[i] == ':':
            word = ''.join(temp)
            arr1.append(word)
            temp = []
            arr1.append(':')
        else:
            # append to temp list if a character
            temp.append(s[i])
    # append last word
    if len(temp) > 0:
        word = ''.join(temp)
        arr1.append(word)

    firstword = arr1[0]
    # find an index of the last word (a delimiter can appear at the end)
    for i in arr1[::-1]:
        if len(i) > 1:
            last = arr1.index(i)
            break
    # Swap the first word and the last word
    arr1[0], arr1[last] = arr1[last], arr1[0]
    # Join back to string
    reversedstr = ''.join(arr1)
    return reversedstr

if __name__ == "__main__":
    s = 'hello//world:here/'
    result = ReverseWordsKeepDelimiters(s)
    print('Original: ', s)
    print('Result: ', result)


# results
# Case 1
# Original: hello/world:here
# Return: here/world:hello

# Case 2
# Original: hello/world:here/
# Return: here/world:hello/

# Case 3
# Original: hello//world:here
# Return: here//world:hello

# Time complexity
# O(n)
