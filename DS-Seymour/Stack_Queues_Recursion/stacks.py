""" Modelling Stack
"""

class stack:
    """ This is modelling of stack
    """
    def __init__(self, size):
        
        self.MAXSTK = size
        self.TOP = 0
        self.full = 0
        self.empty = 1
        
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

stack_1 = stack(5)
stack_1.push(3)
stack_1.push(5)
stack_1.push(7)
stack_1.push(4)
stack_1.push(3)
stack_1.print_info()
pop1 = stack_1.pop()
pop2 = stack_1.pop()
