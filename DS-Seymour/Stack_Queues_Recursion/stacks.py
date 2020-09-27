""" Modelling Stack
"""

from linked_list import *

class stack:
    """ This is modelling of stack
    """
    def __init__(self, size):
        
        self.MAXSTK = size
        self.TOP = 0
        self.full = 0
        self.empty = 1
        self.overflown = 0
        
        self.stack = list()

    def pop(self):

        if not self.TOP:
            print("Stack is already empty")
            self.empty = 1
            return None
        
        popped_item = self.stack[self.TOP - 1]
        self.TOP = self.TOP - 1
        print("Popped item: ", popped_item)
        return popped_item
    
    def push(self, item):

        self.empty = 0

        if self.TOP == self.MAXSTK:
            print("Stack is full. Nothing can be added")
            self.overflown+=1
            return
        
        self.stack.append(item)
        self.TOP+=1

        if self.TOP == self.MAXSTK:
            self.full = 1
    
    def print_info(self):

        print("\n\n=============================")
        print("Below are the stack info")
        print("-----------------------------")
        print("Size: ", self.MAXSTK)
        print("-----------------------------")
        print("Full: ", self.full)
        print("-----------------------------")
        print("Empty: ", self.empty)
        print("-----------------------------")
        print("Current size: ", self.TOP)
        print("-----------------------------")
        print("Contents:\n")
        i = 0
        while (i < self.TOP):
            print(self.stack[i])
            i+=1
        print("=============================")

class linked_stack:

    def __init__(self):
        
        self.MAXSTK = "No size"
        self.TOP = None
        self.full = 0
        self.empty = 1
        self.overflown = 0
    
    def push(self, item):

        node = Node(item)
        node.ptr = self.TOP
        self.TOP = node
    
    def pop(self):
        
        if self.TOP == None:
            print("UNDERFLOW !! .. Stack is empty")
            return

        popped_item = self.TOP
        self.TOP = self.TOP.ptr
        return popped_item.key
    
    def print_info(self):

        if self.TOP == None:
            print("Stack is EMPTY !!")
            return

        node = self.TOP

        while node != None:
            print(node.key)
            node = node.ptr


if __name__ == '__main__' :

    stack_1 = stack(5)
    stack_1.push(3)
    stack_1.push(5)
    stack_1.push(7)
    stack_1.push(4)
    stack_1.push(3)
    stack_1.push(66)
    # stack_1.print_info()
    # pop1 = stack_1.pop()
    # pop2 = stack_1.pop()

    print("------------ LINKED STACK --------------------")

    stack_2 = linked_stack()
    stack_2.pop()
    stack_2.push(2)
    stack_2.push(5)
    stack_2.push(10)
    stack_2.push(1)
    stack_2.print_info()
    print("---")
    k = stack_2.pop()
    k = stack_2.pop()
    k = stack_2.pop()
    k = stack_2.pop()
    # k = stack_2.pop()
    print("popped: ", k)