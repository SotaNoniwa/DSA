
def shell_sort(nums):
    gap = len(nums) // 2

    while gap > 0:
        for i in range(gap, len(nums)):
            j = i

            while j >= gap and nums[j-gap] < nums[j]:
                nums[j], nums[j-gap] = nums[j-gap], nums[j]
                # if swap occurs, we must check previous items in gap steps
                j -= gap
        # decrement the gap
        gap //= 2


if __name__ == '__main__':
    x = [10, -4, 0, 8]
    shell_sort(x)
    print(x)
