# Using Python, write code that will read a file and return the number of capital letters.
# Once you have your initial piece of code, see if you can condense into a one-liner.

def count_capital(file):
    # with open(file, encoding='utf-8') as f:
    #     count = 0
    #     input = f.read()
    #     for i in input:
    #         if i.isupper():
    #             count += 1

    # one line
    count = len([i for f in open(file, encoding='utf-8') for i in f if i.isupper()])

    return count


file = "count_capital_letters.txt"
result = count_capital(file)
print(result)


# Time complexity
# O(len(file))