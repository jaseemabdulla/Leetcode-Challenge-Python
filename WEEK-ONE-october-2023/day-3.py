#  Question No :706. Design HashMap
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def put(self, key, value):
        index = key % self.size
        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
        else:
            current = self.table[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key):
        index = key % self.size
        current = self.table[index]
        if current is None:
            return
        if current.key == key:
            self.table[index] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
            
            
            
            
            