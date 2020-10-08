""" This has basic graph codes
    linked list implementation ..  to be moved to seperate
    -matrix
        -insertion
        -deletion
        -Calc A^n
        -Calc P
        -shortest path
    -list
        -insertion
        -deletion
    -topological sort
"""

class mgraph:

    def __init__(self, glist):
        
        self.nos = len(glist)
        self.glist = glist
    
    def print_mtrx(self, mlist):

        for row in mlist:
            for ele in row:
                print(ele, end=' ')
            print()
        
    def 

if __name__ == '__main__':

    Graph = []
    Graph.append([0, 0, 0, 0, 0])
    Graph.append([0, 0, 0, 0, 0])
    Graph.append([0, 0, 0, 0, 0])
    Graph.append([0, 0, 0, 0, 0])
    Graph.append([0, 0, 0, 0, 0])

    g1 = mgraph(Graph)
    g1.print_mtrx()