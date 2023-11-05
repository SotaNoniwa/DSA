# after heap_sort(), the original heap is not the maximum heap anymore
# it becomes the minimum heap, this might be the problem?

CAPACITY = 10


# maximum heap (root node will be the largest item)
class Heap:
    def __init__(self):
        # this is the actual number of items in the data structure
        self.size = 0
        # the underlying list data structure
        self.heap = [None]*CAPACITY

    # O(logN)
    def insert(self, item):
        if self.size == CAPACITY:
            return

        self.heap[self.size] = item
        self.size += 1

        # check the heap properties
        self.fix_up(self.size-1)

    # starting with the actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # logN it has O(logN) running time complexity
    def fix_up(self, index):
        # you can also separately write for odd or even index, but this is less code
        parent_index = (index-1)//2

        # we consider all the items above till we hit the root node
        # if heap property is  violated then we swap the parent-child
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # peek() return with the max item in O(1)
    def get_max(self):
        return self.heap[0]

    # return the max and remove it as well
    # that is, removing the root node of the heap
    # it has O(logN) running time complexity
    def poll(self):
        max_item = self.get_max()

        # swap the root node with the last item then "heapify"
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size -= 1

        # make sure the heap is "heapify"
        self.fix_down(0)

        return max_item

    # starting with the root node downwards till the heap properties are no longer
    # violated - O(logN)
    def fix_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        # in a max heap the parent is always greater than its children
        largest_index = index

        # looking for the largest (parent or left node)
        if left_index < self.size and self.heap[left_index] > self.heap[largest_index]:
            largest_index = left_index

        # if the right child is greater than the left child
        if right_index < self.size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # if the parent is larger than its children, it's a valid heap
        # so we terminate the recursive method calls
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)

    # it takes O(logN) to get the max AND sorting in O(N) running time
    # O(N) * O(logN) = O(NlogN)
    def heap_sort(self):
        for i in range(self.size):
            max_item = self.poll()
            print(max_item)


if __name__ == '__main__':
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)

    print(heap.heap)
    heap.heap_sort()
    print(heap.heap)
