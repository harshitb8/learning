""" Modelling Stack
"""

class stack:
    """ This is modelling of stack
    """
    def __init__(self, size):
        
        self.MAXSTK = size
        self.TOP = 0
        
        self.stack = list()

    def pop(self):

        if not self.TOP:
            print("Stack is already empty")
            return None
        
        popped_item = self.stack[self.TOP - 1]
        self.TOP = self.TOP - 1
        print("Popped item: ", popped_item)
        return popped_item
    
    def push(self, item):

        if self.TOP == self.MAXSTK:
            print("Stack is full. Nothing can be added")
            return
        
        self.stack.append(item)
        self.TOP+=1

stack_1 = stack(5)
stack_1.push(3)
stack_1.push(5)
pop1 = stack_1.pop()
pop2 = stack_1.pop()
