""" This will have various sorting algorithms
    1. Selection
    2. Bubble
    3. Insertion
    4. Merge
    5. Quick
    6. Radix
    7. Counting
"""

def selection_sort(un_list):

    l = len(un_list)

    i,j = (0, 0)

    for i in range(l):
        min = un_list[i]
        min_idx = i
        for j in range(i, l):
            if min > un_list[j]:
                min = un_list[j]
                min_idx = j

        temp = un_list[i]
        un_list[i] =un_list[min_idx]
        un_list[min_idx] = temp
    
    print("Sorting after Selection Sort: ", un_list)
    return

def bubble_sort(un_list):
    
    l = len(un_list)

    i,j = (0, 0)
    i=l

    while i>=0:
        print("Bubble at i: ", i, " :", un_list)
        print("=============")
        for j in range(i-1):
            print("Bubble at j: ", j, " :", un_list)
            if un_list[j+1] < un_list[j]:
                temp = un_list[j+1]
                un_list[j+1] = un_list[j]
                un_list[j] = temp
        i-=1

    print("Sorting after Bubble Sort: ", un_list)

def insertion_sort(un_list):
    
    l = len(un_list)

    for i in range(1, l):
        element = un_list[i]
        #print("Insertion: at i = ", i, " ", un_list)
        e_idx = i # element index
        j = i-1
        while (un_list[e_idx] < un_list[j] and j>=0):
            temp = un_list[j]
            un_list[j] = un_list[e_idx]
            un_list[e_idx] = temp
            j-=1
            e_idx-=1
    
    print("Sorting after Insertion Sort: ", un_list)


def merge_pass(alist, blist):
    
    la = len(alist)
    lb = len(blist)

    passed = []

    l = min([la, lb])

    while(len(alist) and len(blist)):
        if alist[0] > blist[0]:
            passed.append(blist[0])
            blist = blist[1:]
        elif alist[0] < blist[0]:
            passed.append(alist[0])
            alist = alist[1:]
        elif alist[0] == blist[0]:
            passed.append(blist[0])
            passed.append(alist[0])
            blist = blist[1:]
            alist = alist[1:]
        
    if len(alist):
        for a in alist:
            passed.append(a)
    elif len(blist):
        for b in blist:
            passed.append(b)
    
    return passed

def merge_sort(un_list, l):
    
    if l == 0:
        return
    
    merge_sort(0, 0)


def partition(a, start, end):

    pivot = a[end]


def quick_sort(un_list):
    pass


def radix_sort(un_list):
    pass


def counting_sort(list, start, end):
    pass

if __name__ == '__main__':

    un_list = [5, 8, 9, 6, 1, 7, 3, 0, 4, 2]
    selection_sort(un_list)
    un_list = [5, 8, 9, 6, 1, 7, 3, 0, 4, 2]
    bubble_sort(un_list)
    un_list = [5, 8, 9, 6, 1, 7, 3, 0, 4, 2]
    insertion_sort(un_list)
    # Merge pass
    alist = [1, 3, 5, 7, 9]
    blist = [2, 4, 6, 8, 10, 12, 14]
    merge_pass(alist, blist)