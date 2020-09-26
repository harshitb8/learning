""" insert a node in traversal order
"""

from intro import *
from tree_utils import *

def insert_trav_order(root, key):

    q = []
    q.append(root)

    while(len(q)):

        node = q.pop(0)
        print("HB: debug", node.data)

        if not node.left:
            node.left = Node(key)
            break
        else:
            q.append(node.left)
        
        if not node.right:
            node.right = Node(key)
            break
        else:
            q.append(node.right)



# Driver code
if __name__ == '__main__': 
    root = Node(10)  
    root.left = Node(11)  
    root.left.left = Node(7)  
    root.right = Node(9)  
    root.right.left = Node(15)
    root.right.right = Node(8)

def check_insertion():

    print("print2D traversal before insertion:", end = " ") 
    print2D(root)  
  
    key = 12
    insert_trav_order(root, key)  
  
    print()  
    print("print2D traversal after insertion:", end = " ")
    print(print2D(root))

    key = 121
    insert_trav_order(root, key)  
  
    print()  
    print("print2D traversal after insertion:", end = " ")
    print(print2D(root))