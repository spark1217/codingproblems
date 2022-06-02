# Daily Coding Problem [Medium]
# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. 
# You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. 
# If there's no way to break the text up, then return null.
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
# you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.



def break_lines(str, k):
    words = str.split(' ')
    res = []
    temp = words[0]
    for i in range(len(words)-1):
        if len(temp) + len(words[i+1]) < k:
            temp = temp + ' ' + words[i+1]
        else:
            res.append(temp)
            temp = words[i+1]
    res.append(temp)

    return res

if __name__ == "__main__":
    str = 'the quick brown fox jumps over the lazy dog'
    k = 10
    result = break_lines(str, k)
    print(result)


# Example
# str = 'the quick brown fox jumps over the lazy dog'
# k = 10
# output = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]

# str = 'the quick brown fox jumps over the lazy dog'
# k = 12
# output = ["the quick", "brown fox", "jumps over", "the lazy dog"]

# Time complexity
# O(n)