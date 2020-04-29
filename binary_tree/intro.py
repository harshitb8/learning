"""
this is the code practie for binary tree in gfg tut
"""

class Node(self):

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

class binary_tree(self):

    def __init__(self):
        self.root = None


## ------- testing part build below tree
#       tree
#       ----
#        1    <-- root
#      /   \
#     2     3  
#    /   
#   4

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)