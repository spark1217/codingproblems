# Daily Coding Problem [Easy]
# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.


from itertools import combinations 

def powerset(given_set):
    for i in range(0, len(given_set)+1):
        for element in combinations(given_set, i):
            print("".join(str(element)))
    return


if __name__ == "__main__":
    given_set = [1,2,3]
    powerset(given_set)


# Time complexity
# O(n*2^n)