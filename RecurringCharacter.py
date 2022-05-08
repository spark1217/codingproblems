# Daily Coding Problem [Easy]
# Given a string, return the first recurring character in it, or null if there is no recurring character.
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

def RecurringCharacter(s):
    chars = set()
    for i in s:
        if i not in chars:
            chars.add(i)
        else:
            return i
    return None


if __name__ == "__main__":
    s = "acbbac"
    result = RecurringCharacter(s)
    print(result)


# Examples
# "acbbac" -> b
# "abcdef" -> null

# Time complexity
# O(n)