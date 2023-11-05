# The aim is to design a queue abstract data type with the help of stacks.

class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        # pop the item that we want to dequeue when the item is placed bottom of stack
        # (because Queue is FIFO and Stack is LIFO)
        if len(self.stack) == 1:
            return self.stack.pop()

        # store item to restore it after dequeue
        item = self.stack.pop()

        # recursion
        dequeued_item = self.dequeue()

        # restore item after dequeue
        self.stack.append(item)

        # return the item we want to dequeue
        return dequeued_item


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
