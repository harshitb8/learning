""" Implemention of linked list for graphs
"""

class ll_node:

    def __init__(self, key):

        self.data = key
        self.next = None
    
    def print_ll(self, node):

        if self.node == None:
            return
        
        item = node

        while item != None:
            print(item.data)