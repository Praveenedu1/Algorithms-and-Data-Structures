class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # For chaining

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        head = self.buckets[index]

        # Check if key already exists
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # Insert new node at the head of the chain
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

        # Resize if load factor exceeds threshold
        if self.size / self.capacity > 0.75:
            self._resize()

    def search(self, key):
        index = self._hash(key)
        head = self.buckets[index]

        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def delete(self, key):
        index = self._hash(key)
        head = self.buckets[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.buckets[index] = head.next
                self.size -= 1
                return
            prev = head
            head = head.next

    def _resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity

        for head in self.buckets:
            while head:
                new_index = hash(head.key) % new_capacity
                new_node = HashNode(head.key, head.value)
                new_node.next = new_buckets[new_index]
                new_buckets[new_index] = new_node
                head = head.next

        self.buckets = new_buckets
        self.capacity = new_capacity

# Example usage
ht = HashTable()
ht.insert("key1", "value1")
ht.insert("key2", "value2")
ht.insert("key3", "value3")

print("Search key1:", ht.search("key1"))  # Output: value1
ht.delete("key1")
print("Search key1 after deletion:", ht.search("key1"))  # Output: None
