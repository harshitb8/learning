""" Here we'll see different types of traversaals:
    1.) preorder (statck and recursion)
    2.) inorder (statck and recursion)
    3.) postorder (statck and recursion)
"""

from binary_tree import *

def preorder(root):

    if root == None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)

def preorder_stk(root):

    pass

def inorder(root):

    if root != None:
        print ('==> ', root.data)

    if root == None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):

    if root != None:
        print ('==> ', root.data)

    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data)

def level_trav(root):

    if root == None:
        return
    
    q1 = []

    q1.append(root)

    while len(q1):

        item = q1[0]
        print(item.data)
        q1 = q1[1:]

        if item.left != None:
            q1.append(item.left)
        if item.right != None:
            q1.append(item.right)


if __name__ == '__main__':

    root = bnode(1)
    root.left = bnode(2)
    root.right = bnode(3)

    root.left.left = bnode(4)

    # preorder(root)
    # inorder(root)
    # postorder(root)

    level_trav(root)
    