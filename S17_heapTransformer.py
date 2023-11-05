
class HeapTransformer:

    def __init__(self, heap):
        self.heap = heap

    def transform(self):
        """Transform maximum heap to minimum heap"""
        # truncate leaf nodes, check the property in reverse order
        for i in range((len(self.heap)-2)//2, -1, -1):
            self.fix_down(i)

    def fix_down(self, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        smallest_index = index

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest_index]:
            smallest_index = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        if index != smallest_index:
            self.heap[index], self.heap[smallest_index] \
                = self.heap[smallest_index], self.heap[index]

            self.fix_down(smallest_index)


if __name__ == '__main__':
    heap = HeapTransformer([210, 100, 23, 2, 5])
    heap.transform()
    print(heap.heap)
