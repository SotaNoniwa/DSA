# "TimSort is a hybrid sorting algorithm combining merge sort and insertion sort.
# So when the number of items is less than 32 items then merge sort uses
# insertion sort as a subroutine"
#
# Let's implement TimSort - of course you can use the source code
# of merge sort and insertion sort as well!
#
# For example:
# Input: [1, 7, -4, 105, 837, 34, 96, 47] and
# the output should be the sorted order [-4, 1, 7, 34, 47, 96, 105, 837]

class TimSort:

    def __init__(self, nums):
        # list of integers
        self.nums = nums

    def sort(self):
        self.merge_sort(self.nums)
        return self.nums

    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1

    def merge_sort(self, nums):
        # the merge sort algorithm - you have to use insertion sort when the number of
        # items is less than 32
        if len(nums) < 32:
            self.insertion_sort(nums)
            return

        middle_index = len(nums) // 2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]

        # split the array into two recursively until the items will be less than 32
        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # Then merge two sorted arrays recursively
        self.merge(left_half, right_half, nums)

    def merge(self, left, right, nums):
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    n = [1, 7, -4, 105, 837, 34, 96, 47]
    algorithm = TimSort(n)
    algorithm.sort()
    print(n)
