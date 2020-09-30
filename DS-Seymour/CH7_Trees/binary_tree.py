""" making btree node class for bnode
    binary tree can point to root
"""

class bnode:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

"""
## ------- testing part build below tree
#       tree
#       ----
#            1    <-- root
#          /   \ 
#         2     3  
#        / \     \ 
#       4   5     7
#          / \ 
#         8   9
"""

if __name__ == '__main__':

    root = bnode(1)
    root.left = bnode(2)
    root.right = bnode(3)

    root.left.left = bnode(4)
    root.left.right = bnode(5)

    root.right.right = bnode(7)

    root.left.right.left = bnode(8)
    root.left.right.right = bnode(9)
