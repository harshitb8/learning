"""
To print the tree in level traversal
"""
from tree_utils import *
from intro import *

# ================================== using recursion (tough)

def printLevelOrder(root):
    """ This is using recursion
    """
    print("---- printing below the level traversal of the tree -----")
    
    print("=========================================================")

# Function to  print level order traversal of tree 
def printLevelOrder(root):
    """ This is using recursion
    """
    print("---- printing below the level traversal of the tree -----")
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
    print("=========================================================")
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.data)
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 
  
  
""" Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""
def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

# ==========================================================================
# ==========================================================================
def printLevelOrder_q(root):

    if root == None:
        return
    
    q = []

    q.append(root)

    while(len(q)):

        node = q.pop(0)
        print(node.data)

        if node.left is not None: 
            q.append(node.left) 
  
        # Enqueue right child 
        if node.right is not None: 
            q.append(node.right)

# ============================================================================

# =============== M.A.I.N ====================================================

# Driver program to test above function
if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5)
    root.left.right.right = Node(88)
    
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)
    printLevelOrder_q(root)
    print2D(root)