class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def _hash(self, key):
        return sum(ord(char) for char in key) % 10

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
                pair[1] = value 
                return
        self.table[index].append([key, value])  

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False


ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)

print(ht.get("apple"))
print(ht.get("banana"))   

ht.delete("apple")
print(ht.get("apple"))
