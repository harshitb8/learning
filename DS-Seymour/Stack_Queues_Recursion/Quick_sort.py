""" Quick sort
    1.) Partitioning function
    2.) Use partitioning recursively for sorting
"""

def partitioning(un_list):

    i = 0
    j = len(un_list)

    pivot = un_list[0]

    while (i<j):

        while( un_list[i] >= pivot ):
            i+=1