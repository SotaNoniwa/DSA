# The aim is to design an algorithm that can return the maximum item of a stack in O(1)
# running time complexity. We can use O(N) extra memory!

# Hint: we can use another stack to track the max item

import math


class Stack:
    def __init__(self):
        # this is the actual stack
        self.stack = []
        # this is another stack for getting max value in the actual stack
        self.max_stack = []

    # insert item into the stack
    def push(self, data):
        self.stack.append(data)

        # when data is the first item (no other items in stack)
        if len(self.stack) == 1:
            self.max_stack.append(data)

        # if data is greater than the last item of max_stack, we store the data to max_stack
        # otherwise, we duplicate the last item of max_stack and store it to max_store
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    # remove and return the last item we have inserted (LIFO). O(1)
    def pop(self):
        if self.stack_size() < 1:
            return -1

        # delete the last item to maintain max value
        self.max_stack.pop()

        return self.stack.pop()

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

    def get_max(self):
        if self.stack_size() < 1:
            return -1
        # SOLUTION IN O(1) RUNNING TIME
        return self.max_stack[-1]

        # SOLUTION BUT O(N) TIME COMPLEXITY
        # max_item = -math.inf
        # # O(N) linear running time
        # for item in self.stack:
        #     if max_item < item:
        #         max_item = item
        #
        # return max_item

    def traverse(self):
        for item in self.stack:
            print(item)


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(1)
    stack.push(100)
    stack.push(2)
    stack.push(4)
    stack.traverse()
    print("-"*25)
    print(f"pop: {stack.pop()}")
    print(f"max: {stack.get_max()}")
    print(f"pop: {stack.pop()}")
    print(f"max: {stack.get_max()}")
    print(f"pop: {stack.pop()}")
    print(f"max: {stack.get_max()}")
    print(f"pop: {stack.pop()}")
    print(f"max: {stack.get_max()}")
    print("-"*25)
    stack.traverse()