""" Uses stack to convert expressions to post/pre-fix
"""

from stacks import *

def evaluate_postfix(expr):

    expr = expr.split()
    # expr.append(')')

    tmp_stack = stack(100)
    oprtr = ['+', '-', '*', '/']

    for ele in expr:

        if ele not in oprtr:
            tmp_stack.push(ele)
        
        else:
            pop_1 = int(tmp_stack.pop())
            pop_2 = int(tmp_stack.pop())

            if ele == "+":
                ans = pop_2 + pop_1
                tmp_stack.push(ans)
            if ele == "-":
                ans = pop_2 - pop_1
                tmp_stack.push(ans)
            if ele == "*":
                ans = pop_2 * pop_1
                tmp_stack.push(ans)
            if ele == "/":
                ans = pop_2 / pop_1
                tmp_stack.push(ans)
            
            print("===> ", ans)
        
    return ans
            

if __name__ == '__main__':

    expr = '5 6 2 + * 12 4 / -'
    ans = evaluate_postfix(expr)
    print(ans)

