""" Modelling Linked list
"""

class Node:

    def __init__(self, key):

        self.key = key
        self.ptr = None
    
    def __str__(self):

        print(self.key)