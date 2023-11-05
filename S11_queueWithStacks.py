# The aim is to design a queue abstract data type with the help of stacks.

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        # when there are no items in stacks
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty...")

        # when dequeue_stack is empty, we must add items in O(N) time
        if len(self.dequeue_stack) <= 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        # finally, we pop an item in O(1)
        return self.dequeue_stack.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(20)
    print(queue.dequeue())
    queue.enqueue(100)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())