# Daily Coding Problem [Easy]
# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. 
# You can assume each valid number in the mapping is a single digit.
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

def mapping_digit(digits):
    digitsd = {}
    digitsd['2'] = ['a','b','c']
    digitsd['3'] = ['d','e','f']
    digitsd['4'] = ['g','h','i']
    digitsd['5'] = ['j','k','l']
    digitsd['6'] = ['m','n','o']
    digitsd['7'] = ['p','q','r','s']
    digitsd['8'] = ['t','u','v']
    digitsd['9'] = ['w','x','y','z']

    if len(digits) == 0:
            return []
        
    def backtrack(index, path):
        if len(path) == len(digits):
            output.append("".join(path))
            return 
        possible_letters = digitsd[digits[index]]
        for l in possible_letters:
            path.append(l)
            backtrack(index+1, path)
            path.pop()

    output= []
    backtrack(0,[])
    return output


if __name__ == "__main__":
    s = '23'
    result = mapping_digit(s)
    print(result)


# Time complexity
# O(4^n)