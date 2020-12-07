from Package import Package

class HashTable:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.list = [None] * initial_capacity
        self.size = 0

    def insert(self, key, value):
        if (self.size < self.capacity):
            index = int(key)
            self.list[index] = value
            self.size += 1
        else:
            self.capacity *= 2
            self.size += 1
            index = int(key)
            self.list[index] = value

    def get(self, key):
        return self.list[key]

    def __getitem__(self, key):
        return self.list[key]

