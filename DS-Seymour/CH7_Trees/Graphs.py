""" This has basic graph codes
    linked list implementation ..  to be moved to seperate
    -matrix
        -matrix multiplication .. inclomplete REDO
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

        return self.matrix_mult(self.glist, 1)

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

        pass

    def shortest_path(self):

        """ uses warshall's algoithtm
        """
    
    def convert_to_ll(self):

        """
        """

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