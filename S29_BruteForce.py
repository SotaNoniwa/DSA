
def naive_search(pattern, text):
    # length of the pattern
    m = len(pattern)
    # length of the text
    n = len(text)
    # all indices to return
    indices = []

    # this operation takes O(n) time complexity
    # i.g. we can omit last 2 letters if our pattern consists of more than 2 letters
    for i in range(n-m+1):
        j = 0
        while j < m:
            # if the letter in text and pattern are different
            if text[i+j] != pattern[j]:
                break
            # if the letter in text and pattern are the same, check next letter
            j += 1

        # all letters in pattern are found
        if j == m:
            print(f"Found a match at index {i}")
            indices.append(i)

    return indices


print(naive_search("CD", "ABCCDECD"))
