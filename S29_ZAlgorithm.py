
class ZAlgorithm:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        # we have to concatenate the pattern and text
        self.S = pattern + text
        # int table for Z values
        self.Z = [0 for _ in range(len(self.S))]

    def search(self):
        self.construct_z_table()
        print(self.Z)

        # we just have to consider the values in the Z table in O(N+M)
        for i in range(1, len(self.Z)):
            if self.Z[i] >= len(self.pattern):
                print(f"Match found at index {i-len(self.pattern)}")

    def construct_z_table(self):
        self.Z[0] = len(self.S)

        # the first and last items in the Z box
        left = 0
        right = 0

        # consider all the letters of the S string (starting with index 1)
        for k in range(1, len(self.S)):
            # CASE 1: k (current index) is not within a Z box (naive approach)
            if k > right:
                n = 0

                # when k is in S string and letters are matching,
                # we increment n by 1 then keep comparing the next letter
                while n+k < len(self.S) and self.S[n] == self.S[n+k]:
                    n += 1

                # update the value of Z box at k index
                self.Z[k] = n

                # update left and right (namely, range) of the Z box
                if n > 0:
                    left = k
                    right = k + n - 1
            else:
                # k is inside a Z box (so we can copy the values)
                p = k - left

                # CASE 2: Z[p] value at the prefix is smaller than the rest of the
                # S's substring starting with k in the Z box
                # so we can just copy the value from prefix
                if self.Z[p] < right - k + 1:
                    self.Z[k] = self.Z[p]
                # CASE 3: we can't copy the value
                else:
                    # introduce i index to track outside index of Z box
                    i = right + 1

                    # when i is in S string and letters are matching,
                    # we increment i by 1 then keep comparing the next letter
                    while i < len(self.S) and self.S[i] == self.S[i - k]:
                        i += 1

                    self.Z[k] = i - k
                    left = k
                    right = i - 1


if __name__ == '__main__':
    algorithm = ZAlgorithm("aabza", "abzcaabzaabza")
    algorithm.search()