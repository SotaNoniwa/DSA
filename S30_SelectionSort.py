
# total running time N - 1 * O(N) = O(N*N)
def selection_sort(nums):
    # we make N-1 iterations
    for i in range(len(nums)-1):
        # this variable stores the index of the min item
        index = i

        # this is the LINEAR SEARCH - O(N)
        for j in range(i, len(nums)):
            if nums[j] < nums[index]:
                index = j

        # we have to swap the min item with the left-most item
        # we do not swap the item with itself
        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


if __name__ == '__main__':
    n = [5, 4, 3, 2, 1]
    selection_sort(n)
    print(n)