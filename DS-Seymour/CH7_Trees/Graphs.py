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

        while i < size:
            j = 0
            row = []
            while j < size:
                sum = 0
                k = 0
                while k < size:
                    sum += mata[i][j] * matb[j][i]
                    k += 1
                row.append(sum)
                j += 1
            ans.append(row)
            i += 1
        
        return ans

    
    def get_path_matrix(self):

        """
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