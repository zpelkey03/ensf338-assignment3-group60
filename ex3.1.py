# Right now command line arguments have to use double quotes (")
# instead of single quotes (')

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def is_empty(self):
        return self.head == None

def evaluate(expression):
    stack = Stack()
    expression = expression.replace('(', '').replace(')', '').replace("'", '')
    tokens = expression.split()
    for token in tokens[::-1]:
        if token in ['+', '-', '*', '/']:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            stack.push(result)
        else:
            stack.push(int(token))
    return stack.pop()

if __name__ == '__main__':
    expression = sys.argv[1]
    print(evaluate(expression))