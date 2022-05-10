# Daily Coding Problem [Easy]
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
# ['O', 'B', 'Q', 'P'],
# ['A', 'N', 'O', 'B'],
# ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. 
# Similarly, given the target word 'MASS', you should return true, since it's the last row.

def find_target_word(matrix, word):
    word = word.upper()
    wordpool = []

    # Find words in rows & columns
    for k in range(len(matrix[0])):
        temp = ''
        for j in range(len(matrix)):
            # words in rows
            row = ''.join(matrix[j])
            if row not in wordpool:
                wordpool.append(row)
            # words in columns
            temp += matrix[j][k]
        wordpool.append(temp)

    for w in wordpool:
        if word in w:
            return True
    return False


if __name__ == "__main__":
    matrix = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
    word = 'Foam'
    result = find_target_word(matrix, word)
    print(result)


# Example
# 'FACE' --> False
# 'FOAM' --> True

# Time complexity
# O(n^2)