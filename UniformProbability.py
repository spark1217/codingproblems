# Daily Coding Problem [Easy]
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).

import random

def rand7():
    return random.randint(1,7)

def rand5():
    n = 7*rand7() + rand7() - 7
    if n > 45:
        return rand5()
    return n%5+1


if __name__ == "__main__":
    print('rand7: ', rand7())
    print('rand5: ', rand5())