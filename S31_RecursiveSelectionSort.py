# We have seen in the previous chapters how to implement selection sort
# with iteration. Because it is absolutely crucial to understand recursion
# in computer science: your task is to construct the recursive selection sort algorithm!
#
# Of course the aim is to sort an underlying list:
#
# Input is for example [1, 7, -4, 105, 837, 34, 96, 4500] and the output should be
# the sorted order [-4, 1, 7, 34, 96, 105, 837, 4500]


class RecursiveSelectionSort:

    def __init__(self, nums):
        # this is the list we want to sort
        self.nums = nums

    def sort(self):
        self.selection_sort()
        return self.nums

    def find_min(self, i, j):
        # find the minimum item recursively
        # i: index of actual item
        # j: index of last item
        if i == j:
            return i

        k = self.find_min(i+1, j)

        if self.nums[i] < self.nums[k]:
            return i
        else:
            return k

    def selection_sort(self, index=0):
        # selection sort algorithm starting with index (first item which is index 0)
        if index == len(self.nums):
            return -1

        k = self.find_min(index, len(self.nums) - 1)

        if k != index:
            self.nums[k], self.nums[index] = self.nums[index], self.nums[k]

        self.selection_sort(index + 1)


if __name__ == '__main__':
    x = [1, 7, -4, 105, 837, 34, 96, 4500]
    sort = RecursiveSelectionSort(x)
    sort.sort()
    print(x)
