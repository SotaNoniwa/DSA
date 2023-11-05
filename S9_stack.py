# Stacks are LIFO
# Stack is abstract data type, array or linked list can be data structure of its implementation

class Stack:
    def __init__(self):
        self.stack = []

    # insert item into the stack
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have inserted (LIFO). O(1)
    def pop(self):
        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek: it returns the last item without removing it. O(1)
    def peek(self):
        if self.stack_size() < 1:
            return -1

        return self.stack[-1]

    # has O(1) running time
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Size: {stack.stack_size()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Size: {stack.stack_size()}")
    print(f"Peek item: {stack.peek()}")
    print(f"Size: {stack.stack_size()}")

