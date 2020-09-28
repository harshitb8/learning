""" Tower of Hanoi problem
    we'll pass number of discs and tower names
"""

def tower_of_hanoi(n, beg, aux, end):

    """ Uses recursion
        Tohought process: we can move the top n-1 discs
        using the any of them as auxilarry
    """
    # print('here')

    if n == 1:
        print(beg, ' -> ', end)
        return
    
    tower_of_hanoi(n-1, beg, end, aux)
    print(beg, ' -> ', end)
    tower_of_hanoi(n-1, aux, beg, end)
    return

def tower_of_hanoi_stack(n, beg, aux, end):

    """ Here, we'll implement the above using stack
    """


if __name__ == '__main__':

    tower_of_hanoi(3, 'A', 'B', 'C')
