""" This is implementation of queue
    1.) straight ..  but it's expensive .. so..
    2.) circular structure
    3.) using linked list
"""

from linked_list import *

class queue:

    def __init__(self, size):

        # Will take front as always 0
        self.rear = -1
        self.max = size
        self.qu = [None] * self.max
    
    def Qinsert(self, item):
        
        if self.rear == self.max - 1:
            print("Queue is filled !!")
            return

        self.rear += 1
        self.qu[self.rear] = item
    
    def Qdelete(self):

        if self.rear < 0:
            print("Queue is Empty !!!")
            return

        deleted_item = self.qu[0]

        for k in range(self.rear):
            self.qu[k] = self.qu[k + 1]
        
        self.rear -= 1

        return deleted_item
    
    def print_info(self):

        print(self.qu[0:self.rear+1])

class queue_link:

    def __init__(self):

        self.front = Node(None)
        self.rear = Node(None)

    def Qinsert(self, item):

        node = Node(item)
        
        if self.front.key == None:
            self.front = node
            self.rear = node
        else:
            self.rear.ptr = node
            self.rear = node
        
    def Qdelete(self):

        if self.front.key == None:
            print('Queue is empty !!')
            return
        
        deleted_item = self.front.key

        self.front = self.front.ptr

        return deleted_item
    
    def print_info(self):

        print ('-- queue below --')

        node = self.front

        while node.ptr != None:
            print(node.key)
            node = node.ptr
        
        print(node.key)

        print ('-----------------')

class deques:

    def __init__(self):

        pass

class p_queue:

    def __init__(self, size):

        """ This is a Priority queue where list of 2 elements in passed
        """

        # Will take front as always 0
        self.rear = -1
        self.max = size
        self.qu = [None] * self.max
            

if __name__ == '__main__':

    queue_1 = queue(6)
    queue_1.Qdelete()
    queue_1.Qinsert(2)
    queue_1.Qinsert(10)
    k = queue_1.Qdelete()
    k = queue_1.Qdelete()
    print("Deleted: ", k)
    queue_1.print_info()
    queue_1.Qinsert(7)
    queue_1.print_info()
    print('---- Link Q Below ----')
    queue_2 = queue_link()
    queue_2.Qinsert(5)
    queue_2.Qinsert(10)
    queue_2.Qinsert(11)
    queue_2.Qinsert(12)
    queue_2.Qinsert(13)
    queue_2.Qinsert(14)
    queue_2.Qinsert(15)
    queue_2.Qinsert(16)
    queue_2.print_info()
    k = queue_2.Qdelete()
    k = queue_2.Qdelete()
    k = queue_2.Qdelete()
    k = queue_2.Qdelete()
    k = queue_2.Qdelete()
    k = queue_2.Qdelete()
    print('Linked Queue deleted item: ', k)
    queue_2.print_info()
    # print("start and end: ", queue_2.front.key, queue_2.rear.key)


