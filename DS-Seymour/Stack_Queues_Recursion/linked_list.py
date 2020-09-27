""" Modelling Linked list
"""

class Node:

    def __init__(self, key):

        self.key = key
        self.ptr = None
    
    def __str__(self):

        print(str(self.key))



if __name__ == "__main__":

    node = Node(5)
    print(node.key)