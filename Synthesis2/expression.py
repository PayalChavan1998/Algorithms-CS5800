# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -2
# Topic: Depth-First-Search (DFS)
# Date: 07/10/2024


'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
'''

# Initialize Left & Right side of node
LEFT = 0
RIGHT = 1

# Define nodes left, right, root
class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# Define a function evaluate() that takes node
def evaluate(node: Node):
    # if we found the numeric node then thats a leaf node
    if (node.val.isnumeric()):
        return int(node.val)

    # traverse left
    left_val = evaluate(node.left)

    # traverse right
    right_val = evaluate(node.right)

    # evaluate expression (LEFT_VALUE, ROOT_OPERATOR, RIGHT_VALUE)
    return (
        ( node.val == '+' and left_val + right_val ) or
        ( node.val == '-' and left_val - right_val ) or
        ( node.val == '*' and left_val * right_val ) or
        ( node.val == '/' and left_val // right_val )
    )



# create a expression tree
def buildTree(postfix: list):
    root = None
    stack = []

    while (postfix):
        # remove last element and create node
        curr = postfix.pop()
        curr_node = Node(curr)

        # if root node is not set then set the current node as root node
        if (not root):
            root = curr_node
        
        # if stack is not empty, then parent => delete last element from stack
        if (stack):
            parent, side = stack.pop()

            # if side is same as LEFT, then
            if (side == LEFT):
                parent.left = curr_node
            else:
                parent.right = curr_node
        

        # if current node is not numeric then it will have 2 children nodes
        if (not curr.isnumeric()):
            stack.append((curr_node, LEFT))
            stack.append((curr_node, RIGHT))

    return root


# Driver program to test the code
if __name__ == '__main__':
    root = buildTree(['1', '2', '+', '6', '*', '9', '3', '-', '2', '/', '+'])
    print(evaluate(root))

'''
Output:
/usr/bin/python3 /Users/payalchavan/Documents/Algorithms/Synthesis2/expression.py
21
'''
