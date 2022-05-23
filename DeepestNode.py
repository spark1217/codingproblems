# Daily Coding Problem [Easy]
# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
#     a
#    / \
#   b   c
#  /
# d

import queue

class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def deepest_node(root):
    if root is None:
        return None
    
    node = None
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return node.data

root = node('a')
root.left = node('b')
root.right = node('c')
root.left.left = node('d')
print(deepest_node(root))


# Time complexity
# O(n)