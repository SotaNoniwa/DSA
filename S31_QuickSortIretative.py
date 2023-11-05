# We have considered the theory as well as the implementation of QuickSort.
# It is a typical divide and conquer algorithm so we have used recursion.
# Your task is to solve the same problem without recursion.
#
# NOTE: you can use a stack abstract data type on your own instead of using
# the OS stack memory during recursion. Let's use the doubly linked list
# implementation of from collections import deque abstract data type of Python.
#
# You can insert new items with the append() method and you can remove items
# with the pop() method!
#
# Example: if the input is [5, 4, 3, 2, 1] then the output should be the
# sorted order [1, 2, 3, 4, 5]

from collections import deque


class QuickSortIterative:
    def __init__(self, data):
        self.data = data

    def sort(self):
        # create stack
        stack = deque()

        # store the first and last indexes as a tuple
        stack.append((0, len(self.data) - 1))

        while stack:
            # extract the first and last indexes i.g. stack[(0,4)] then
            # pop() returns (0,4), thus start = 0, end = 4
            start, end = stack.pop()

            pivot = self.partition(start, end)

            # CONQUER PHASE
            # consider the left sub-array
            if pivot - 1 > start:
                stack.append((start, pivot - 1))

            # consider the right sub-array
            if pivot + 1 < end:
                stack.append((pivot + 1, end))

    def partition(self, low, high):
        pivot_index = (low + high) // 2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high, 1):
            if self.data[j] <= self.data[high]:
                self.data[j], self.data[low] = self.data[low], self.data[j]
                low += 1

        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low


if __name__ == '__main__':
    n = [5, 4, 3, 2, 1]
    algorithm = QuickSortIterative(n)
    algorithm.sort()
    print(algorithm.data)
