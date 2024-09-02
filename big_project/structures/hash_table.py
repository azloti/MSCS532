class HashTable:

    # Initialize the hash table with a given size
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function to determine the index of a key
    def _hash_function(self, key):
        return hash(key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    # Search for a key in the hash table and return its value
    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    # Delete a key-value pair from the hash table
    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return

    # Display the contents of the hash table
    def display(self):
        for index, items in enumerate(self.table):
            print(f"Index {index}: {items}")