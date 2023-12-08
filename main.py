class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def check_balanced(expression):
    stack = Stack()
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for char in expression:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[
                stack.pop()] != char:
                return False

    return stack.is_empty()



expressions = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{",
    "{{[(])]}}",
    "[[{())}]"
]

for expression in expressions:
    if check_balanced(expression):
        print(f"Скобки в выражении {expression} сбалансированы.")
    else:
        print(f"Скобки в выражении {expression} несбалансированы.")