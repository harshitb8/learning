""" This has basic graph codes
    linked list implementation ..  to be moved to seperate
    -matrix
        -matrix multiplication .. inclomplete REDO
        -insertion
        -deletion
        -Calc A^n
        -Calc P
        -shortest path.. Getting incorrect output
    -list
        -insertion
        -deletion
    -topological sort
"""

from linked_list_for_graphs import *

class mgraph:

    def __init__(self, glist):
        
        self.nos = len(glist)
        self.glist = glist
    
    def print_mtrx(self, **kwargs):

        try:
            mlist = kwargs['mlist']
        except:
            mlist = self.glist

        for row in mlist:
            for ele in row:
                print(ele, end=' ')
            print()
        
    def get_adjency_matrix(self):

        """ This would be matrix passed ^ 1
        """

        return self.A_to_m(1)

    def A_to_m(self, m):

        """ This returns the A to the power m
        """
        
        if m == 0:
            return 1

        A = self.glist

        ans = A
        i = 1
        while i < m:
            ans = self.matrix_mult(ans, A)
            i += 1

        return ans

    def matrix_mult(self, mata, matb):
        
        """ This returns the matrix A * matrix B
            Assumption .. has to be equal sq matrices
        """

        ans = []
        size = len(mata)
        i = 0

        X = mata
        Y = matb

        result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

        return result
 
    def get_path_matrix(self):

        """ returns the Path Matrix 1 if there exist any path
            Bm  = A + A^2 + ... A^m
        """

        # Calculating Bm // m = self.nos

        B = [[0] * self.nos] * self.nos
        P = [[0] * self.nos] * self.nos
        i = 1

        while i <= self.nos:

            mat = self.A_to_m(i)

            # adding matrices B= B + mat
            B = self.sum_of_matrices(B, mat)
            i+=1
        
        # return B

        ans = []

        for row in B:
            row_ans = []
            for ele in row:
                if ele != 0:
                    row_ans.append(1)
                else:
                    row_ans.append(0)
            ans.append(row_ans)
        
        return ans
    
    def sum_of_matrices(self, mata, matb):

        """ Copied
        """

        X = mata
        Y = matb

        result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

        return result

    def warshall_path_m(self):

        """ getting path matrix wihoiut multiplication
        """

        P = self.get_adjency_matrix()

        for k in range (self.nos):
            for i in range(self.nos):
                for j in range(self.nos):
                    P[i][j] = P[i][j] | ( P[i][k] & P[k][j] )
        
        return P

    def shortest_path(self):

        """ uses warshall's algoithtm to find the shortest path
            weighted graphis passed
        """

        # replace 0 with 100

        Q = [[0]*self.nos]*self.nos
        Q = []

        for i in range(self.nos):
            q_row = []
            for j in range(self.nos):
                if self.glist[i][j] == 0:
                    q_row.append(100)
                else:
                    q_row.append(self.glist[i][j])
            Q.append(q_row)
        
        Q_temp = []
        for k in range(self.nos):
            # print('-------------', k)
            # self.print_mtrx(mlist = Q)
            # print()
            for i in range(self.nos):
                Q_temp_row = []
                for j in range(self.nos):
                    Q[i][j] = min([ Q[i][j], Q[i][k] + Q[k][j] ])
                    value = min([ Q[i][j], Q[i][k] + Q[k][j] ])
                    Q_temp_row.append(value)
                Q_temp.append(Q_temp_row)
            
            # Q = Q_temp

        
        return Q
    
    def convert_to_ll(self):

        """
        """

def print_ll_graph(node):

    if node == None:
        return
    
    node_list_item = node

    while node_list_item != None:

        print(f'{node_list_item.data}:', end = ' ')

        adj_item = node_list_item.adj
        print(adj_item, end = ' ')
        
        node_list_item = node_list_item.next
        print()

if __name__ == '__main__':

    Graph = []
    Graph.append([0, 0, 0, 1])
    Graph.append([1, 0, 1, 1])
    Graph.append([1, 0, 0, 1])
    Graph.append([0, 0, 1, 0])

    g1 = mgraph(Graph)
    g1.print_mtrx()
    print()

    # k = g1.A_to_m(3)
    k = g1.get_path_matrix()
    g1.print_mtrx(mlist = k)
    print()
    k = g1.warshall_path_m()
    g1.print_mtrx(mlist = k)
    print()

    WGraph = []
    WGraph.append([7, 5, 0, 0])
    WGraph.append([7, 0, 0, 2])
    WGraph.append([0, 3, 0, 0])
    WGraph.append([4, 0, 1, 0])

    wg1=mgraph(WGraph)
    k = wg1.shortest_path()
    wg1.print_mtrx(mlist = k)
    print()

    print(' ---------------- LINKED LIST GRAPH --------------')

    # Page: 8.12

    graph_nodes = ['A', 'B', 'C', 'D', 'E']
    node_list = list_to_ll(graph_nodes)
    
    # print_ll(node_list)

    # for A
    node_list.adj = ll_node(node_list.next)

    # ---------------------------------------------------------------
    # Understand the edge list pointed by adj stores the location
    #   of the node and that has data
    # print(node_list)
    # print(node_list.data)
    # print(node_list.adj)
    # print(node_list.adj.data)
    # print(node_list.adj.data.data)
    # ---------------------------------------------------------------

    node_list.adj.next = ll_node(node_list.next.next)
    node_list.adj.next.next = ll_node(node_list.next.next.next)

    # for B
    node_list.next.adj = ll_node(node_list.next.next)

    # for C
    node_list.next.next.adj = None
    
    # for D
    node_list.next.next.next.adj = ll_node(node_list.next.next)
    node_list.next.next.next.adj.next = ll_node(node_list.next.next.next.next)

    # for E
    print('===')
    print(node_list.next.next.next.next.data)
    node_list.next.next.next.next.adj = ll_node(node_list.next.next)
    
    print_ll_graph(node_list)
