class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow!"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty!"
        return self.stack[-1]

    def display(self):
        return self.stack[::-1]

    def is_empty(self):
        return len(self.stack) == 0


def delimiter_matching(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


def prefix_to_postfix(prefix):
    stack = []

    for ch in reversed(prefix):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + ch)

    return stack[-1]


def evaluate_postfix(postfix):
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)
            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()