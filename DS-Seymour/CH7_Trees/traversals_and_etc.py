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

    """ preorder using stack
    """

    if root == None:
        return
    
    stk = []

    stk.append(root)

    while len(stk):

        item = stk.pop()

        while item != None:
            
            print(item.data)
            stk.append(item.right)
            item = item.left

def inorder(root):

    if root != None:
        print ('==> ', root.data)

    if root == None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

def inorder_stk(root):

    print('================')

    if root == None:
        return
    
    stk = []

    item = root

    while item != None:
        
        stk.append(item)
        item = item.left
    
    while len(stk):

        item = stk.pop()
        print(item.data)

        if item.right != None:
            item = item.right

            while item != None:
        
                stk.append(item)
                item = item.left

def postorder(root):

    if root != None:
        print ('==> ', root.data)

    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data)

def postorder_stk(root):

    if root == None:
        return

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

def delete_node(root, node):

    """ deletes the node and replces it with the last level
        trav node if internal node
        root is taken just if the node is internal (not leaf)
        and that case last node will be found wrt to the root
        passed
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

    # preorder(root)
    # inorder(root)
    # postorder(root)

    inorder_stk(root)
    