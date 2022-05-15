# Daily Coding Problem [Easy]
# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.


def encoding(s):
    count = 1
    encoded = ''
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            encoded += str(count) + s[i]
            count = 1
        else:
            count += 1
    encoded += str(count) + s[len(s)-1]
    return encoded

def decoding(s):
    # if index % 2 == 0, can be converted to integer
    # if index % 2 == 1, it is a character.
    decoded = ''
    for i in range(len(s)-1):
        if i % 2 == 0:
            for j in range(int(s[i])):
                decoded += s[i+1]

    return decoded

if __name__ == "__main__":
    encoding_input = 'AAAABBBCCDAA'
    decoding_input = '4A3B2C1D2A'
    encoding_result = encoding(encoding_input)
    decoding_result = decoding(decoding_input)
    print(encoding_input, ' --> ', encoding_result)
    print(decoding_input, ' --> ', decoding_result)


# Example
# Encoding : AAAABBBCCDAA --> 4A3B2C1D2A
# Decoding : 4A3B2C1D2A --> AAAABBBCCDAA


# Time complexity
# Encoding O(n)
# Decoding O(n^2)