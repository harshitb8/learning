""" Quick sort
    1.) Partitioning function
    2.) Use partitioning recursively for sorting
"""

def partitioning(un_list, lb, ub):

    """ Finding out the proper place for pivot element is
        known as partitioning
    """

    i = lb
    j = ub

    pivot = un_list[0]
    print('------')
    print("Before Partitioning", un_list)

    while ( i<j ):

        # print('------')

        while( un_list[i] <= pivot ):
            i+=1

        # print('i: ', i)

        while( un_list[j] > pivot ):
            j-=1

        # print('j: ', j)

        if (i<j):
            temp = un_list[i]
            un_list[i] = un_list[j]
            un_list[j] = temp

        # print(un_list)
    
    un_list[0] = un_list[j]
    un_list[j] = pivot

    print("After partitioning: ", un_list)

    return j
             
def quick_sort(un_list, lb, ub):

    """ Use Partitioning recursively for sorting
    """

    if lb < ub:
        loc = partitioning(un_list, lb, ub)
        quick_sort(un_list, lb, loc-1)
        quick_sort(un_list, loc+1, ub)
    else: 
        return

if __name__ == '__main__':

    un_list = [7, 6, 10, 5, 9, 2, 1, 15, 89]

    # k = partitioning(un_list, 0, 8)
    # print(k)
    quick_sort(un_list, 0, 8)
    print(un_list)