# Queue is an abstract data type, FIFO
# array or linked list can be underlying data structures

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    # O(1) running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time. Doubly linked list can reduce time complexity to O(1).
    def dequeue(self):
        if self.size_queue() > 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    # O(1) running time
    def peek(self):
        if self.size_queue() > 1:
            return self.queue[0]
        else:
            return -1

    # O(1) running time
    def size_queue(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Size: {queue.size_queue()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Peak: {queue.peek()}")
    print(f"Size: {queue.size_queue()}")