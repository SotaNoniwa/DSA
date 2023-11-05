
class RabinKarp:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.alphabet_size = 26
        self.prime = 31

    def search(self):
        pattern_l = len(self.pattern)
        text_l = len(self.text)

        hash_text = 0
        hash_pattern = 0

        # the largest polynomial term in the fingerprint function
        # i.g. h = (26*26*26)%31 for 3 letters
        h = 1
        for _ in range(pattern_l - 1):
            h = (h * self.alphabet_size) % self.prime

        # produce hash values
        for i in range(pattern_l):
            hash_pattern = (self.alphabet_size * hash_pattern + ord(self.pattern[i])) % self.prime
            hash_text = (self.alphabet_size * hash_text + ord(self.text[i])) % self.prime

        # slide the pattern over text one by one
        for i in range(text_l - pattern_l + 1):
            if hash_text == hash_pattern:
                j = 0

                while j < pattern_l:
                    if self.text[i+j] != self.pattern[j]:
                        break
                    j += 1

                if j == pattern_l:
                    print(f"Found match at index {i}")

            # rolling hash: slide window one by one
            # i.g. pattern is "AB", text is "XAB", we need 2 iteration. i will be 0, 1, stop
            if i < text_l - pattern_l:
                # "XA" is a first window (when i is 0), "AB" is a second window (i is 1)
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.alphabet_size + ord(self.text[i + pattern_l])) % self.prime

                # we might get negative value, so we must make sure the hash is positive
                if hash_text < 0:
                    hash_text += self.prime


if __name__ == '__main__':
    algorithm = RabinKarp("test", "this is a test")
    algorithm.search()
