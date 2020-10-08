""" Heaps
    Check if complete bin tree
    Complete Bin tree to array - Done
    Array to binary tree
    Heaps insertion
    Heaps Deletion - Incomplete
    All above implemented in Maxheap ....convert it to min heap -Incomplete
"""

from binary_tree import *
from tree_utils import *
import math

def bintree_to_array(root):

    if root == None:
        print('Empty tree passed')
        return []

    array = []
    q = []

    q.append(root)

    while len(q):

        item = q[0]
        array.append(item.data)
        q = q[1:]

        if item.left != None:
            q.append(item.left)
        
        if item.right != None:
            q.append(item.right)
        

    return array

def array_to_comp_bin_tree(array):

    if not len(array):
        return []

    node_array = list(map(lambda x : bnode(x), array))
    len_arr = len(array)

    i = 0
    for item in node_array:
        
        left_idx = 2*i + 1
        right_idx = 2*i + 2

        if left_idx < len_arr:
            item.left = node_array[left_idx]
        else:
            item.left = None
        
        if right_idx < len_arr:
            item.right = node_array[right_idx]
        else:
            item.right = None
        
        i += 1
    
    root = node_array[0]
    return root
    
def insert_in_heap(array, key):

    """ This function inserts in heap
        heap is passed as array representaion of tree
    """

    array.append(key)

    idx = len(array) - 1

    while idx > 0:
        
        par_idx = math.floor((idx - 1)/2)
        if array[idx] > array[par_idx]:
            temp = array[idx]
            array[idx] = array[par_idx]
            array[par_idx] = temp
            idx = par_idx
        else:
            break
    
    return array

def delete_root_from_heap():
    pass

if __name__ == '__main__':

    root = bnode(1)
    root.left = bnode(2)
    root.right = bnode(3)

    root.left.left = bnode(4)
    root.left.right = bnode(5)

    root.right.right = bnode(7)

    root.left.right.left = bnode(8)
    root.left.right.right = bnode(9)

    arr = bintree_to_array(root)
    cmpl_root = array_to_comp_bin_tree(arr)
    print2D(cmpl_root)

    print('===============')

    print2D(array_to_comp_bin_tree(insert_in_heap([11], 6.5)))

