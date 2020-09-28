""" Quick sort
    1.) Partitioning function
    2.) Use partitioning recursively for sorting
"""

def partitioning(un_list):

    """ Finding out the proper place for pivot element is
        known as partitioning
    """

    i = 0
    j = len(un_list) - 1

    pivot = un_list[0]
    print(un_list)

    for k in range(1):


        while( un_list[i] >= pivot ):
            i+=1

        while( un_list[j] <= pivot ):
            j-=1

        if (i<j):
            temp = un_list[i]
            un_list[i] = un_list[j]
            un_list[j] = temp
        
        print(un_list)
             

if __name__ == '__main__':

    un_list = [7, 6, 10, 5, 9, 2, 1, 15, 7]

    partitioning(un_list)