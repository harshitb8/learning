""" Searching in BST
"""

from binary_tree import *
from tree_utils import *

def search_in_bst(root, key):
    
    if root == None:
        print('Empty Tree Passed')
        return
    
    level = 0

    item = root

    while item != None:

        if item.data == key:
            print('Found at level: ', level)
            return

        if key > item.data:
            item = item.right    
        elif key < item.data:
            item =  item.left
    
        level += 1
    
    print('Search Unuccessful')

def insert_in_bst(root, key):
    
    if not isinstance(key, list):
        keys = [key]
    else:
        keys = key

    for key in keys:

        if root == None:
            root = bnode(key)
            break
        
        level = 0

        item = root

        while item != None:

            if item.data == key:
                print('Already in BST: ', level)
                break

            if key > item.data:
                if item.right == None:
                    item.right = bnode(key)
                    break
                else:
                    item =  item.right    
            elif key < item.data:
                if item.left == None:
                    item.left = bnode(key)
                    break
                else:
                    item =  item.left
        
            level += 1


def delete_in_bst(root, key):
    pass

"""
## ------- testing part build below BST tree ----
#       
#       
#            38    <-- root
#          /    \ 
#        14      56  
#       /  \    /  \ 
#      8    23 45   82 
#          /       /
#         18      70
"""

if __name__ == '__main__':

    # create a binary search tree

    root = bnode(38)
    
    root.left = bnode(14)
    root.right = bnode(56)

    root.left.left = bnode(8)
    root.left.right = bnode(23)

    root.left.right.left = bnode(18)

    root.right.left = bnode(45)
    root.right.right = bnode(82)

    root.right.right.left = bnode(70)

    insert_in_bst(root, [24, 100])
    # print('------------------')
    # print2D(root)
