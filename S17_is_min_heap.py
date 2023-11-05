
def is_min_heap(heap):
    if len(heap) <= 1:
        return True

    if len(heap) == 2:
        return heap[0] < heap[1]

    # this formula truncate leaf nodes as there's no need to check them
    num_items = (len(heap) - 2) // 2 + 1

    # running time is O(N) linear
    for i in range(num_items):
        if heap[i] > heap[i*2+1] or heap[i] > heap[i*2+2]:
            return False

    return True


if __name__ == '__main__':
    heap = [1, 3, 2, 4, 5]
    print(is_min_heap(heap))