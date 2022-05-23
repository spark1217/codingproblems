# Daily Coding Problem [Easy]
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

def readn(s, n):
    i = 0
    if len(s) < n:
        return print(s)
    
    while len(s) >= n:
        print(s[i:i+n])
        s = s[i+n:]
    print(s)
    print("")
    return


if __name__ == "__main__":
    s = 'Hello world'
    n = 7
    readn(s, n)
    

# Example
# s = 'Hello world'
# n = 7
# Return "Hello w", "orld", ""

# Time complexity
# O(n)