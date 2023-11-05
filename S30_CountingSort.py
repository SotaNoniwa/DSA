
class CountingSort:
    def __init__(self, data):
        self.data = data
        # k = max - min + 1 where k is the size of count_array
        self.count_array = [0 for _ in range(max(data) - min(data) + 1)]

    def sort(self):
        for i in range(len(self.data)):
            # indices start with 0, we should handle negative values as well
            # To deal with these problems, we subtract minimum value
            self.count_array[self.data[i] - min(self.data)] += 1

        # we have to consider the counting array in O(k)
        z = 0
        for i in range(min(self.data), max(self.data) + 1):
            while self.count_array[i - min(self.data)] > 0:
                self.data[z] = i
                z += 1
                self.count_array[i - min(self.data)] -= 1


if __name__ == '__main__':
    n = [4, 6, -3, 0, 10, 14, 22, 5]
    counting_sort = CountingSort(n)
    counting_sort.sort()
    print(counting_sort.data)