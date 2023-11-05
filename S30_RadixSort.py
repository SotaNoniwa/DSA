import random

ITEMS_IN_BUCKETS = 10


class RadixSort:
    def __init__(self, data):
        self.data = data

    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, digit):
        # initialize an empty inner-array * 10 (ITEMS_IN_BUCKETS) who's indices
        # represents 0-9 digits in an outer-array
        count_array = [[] for _ in range(ITEMS_IN_BUCKETS)]

        # store the count of each element in count array
        for num in self.data:
            # calculate the index of the given bucket
            index = (num // (10 ** digit)) % 10
            count_array[index].append(num)

        # we have to consider all the items in the count array (list)
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0:
                # it takes O(N) linear running time complexity
                # if we use the dictionary, it takes O(1) but need extra memory
                self.data[z] = count_array[i].pop(0)
                z += 1


if __name__ == '__main__':
    n = [5, 3, 10, 12, 9, 8, 20, 100, 325, 1023]
    random.shuffle(n)
    print(n)
    radix_sort = RadixSort(n)
    radix_sort.sort()
    print(radix_sort.data)
