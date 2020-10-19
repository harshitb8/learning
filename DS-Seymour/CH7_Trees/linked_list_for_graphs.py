""" Implemention of linked list for graphs
"""

class ll_node:

    def __init__(self, key):

        self.data = key
        self.next = None
        self.adj = None
    
    def print_ll(self, node = None, end = '\n'):

        if node == None:
            return
        
        item = node

        while item != None:
            print(item.data, end = end)
            item = item.next
        
        if end != '\n':
            print()

def print_ll(node = None, end = '\n'):

    if node == None:
        return
    
    item = node

    while item != None:
        print(item.data, end = end)
        item = item.next
    
    if end != '\n':
        print()
    
def list_to_ll(nrml_list):
        
        if not len(nrml_list):
           return None
        
        node = ll_node(nrml_list[0])
        start = node

        for k in nrml_list[1:]:
            node.next = ll_node(k)
            node = node.next
        
        return start

if __name__ == '__main__':

    a = ll_node('A')
    a.next = ll_node('B')
    a.next.next = ll_node('C')
    a.next.next.next = ll_node('D')
    a.next.next.next.next = ll_node('E')

    # a.print_ll(node = a, end = ' -> ')

    n_list = [1, 2, 3, 4]

    ll = list_to_ll(n_list)
    print_ll(node = ll, end = ' -> ')
