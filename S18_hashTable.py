
class HashTable:
    def __init__(self):
        # based on the load factor, we may change the size of the underlying
        # data structure (dynamic resizing)
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    # hash value (index of the array) based on the key
    def hash_function(self, key):
        hash_sum = 0

        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity

    def insert(self, key, data):
        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        # there may be collisions which means that the index is already occupied
        # while we don't find an empty array slot
        while self.keys[index] is not None:
            # we just update the value if the key is already present
            if self.keys[index] == key:
                self.values[index] = data
                return

            # do linear probing (try the next slot in the array)
            # because we may increment the index to find available slot
            index = (index + 1) % self.capacity

        # we have found the valid slot for the item, so we can insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        # the given key doesn't exist in the hashtable
        return None


if __name__ == '__main__':
    table = HashTable()
    table.insert("Adam", 23)
    table.insert("Kevin", 45)
    table.insert("Daniel", 34)
    table.insert("Daniel", 33)

    print(table.get("Daniel"))
