# This is a custom direct access hash table.
# This upside of this type of hash table is it always allow for O(1) access time, since only one object will occupy each bucket.  
# The downside is that the space complexity is equal to the number of objects that the hash table must hold.
# When dealing with a relatively small number of objects it is simple to implement and should have no issues.
# If there were a large amount of items, then this method could take up too much space.
# The hash table automatically adjusts it's capacity if the current size is not less than the current capacity.
# This makes it self-adjusting.
class HashTable:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.list = [None] * initial_capacity
        self.size = 0

    # This function allows a key-value pair to be inserted into the hash table. 
    # It has a time complexity of O(N) and a space complexity of O(N).
    def insert(self, key, value):
        if (self.size < self.capacity - 1):
            index = int(key)
            self.list[index] = value
            self.size += 1
        else: 
            index = int(key)
            self.capacity += 1
            self.size += 1
            temp_list = [None] * self.capacity
            for i in range(len(self.list)):
                temp_list[i] = self.list[i]
            self.list = temp_list
            self.list[index] = value


    # This function allows one to retrieve a value by entering a key as the parameter to the method.
    # It has a time complexity of O(1) and a space complexity of O(1).
    def get(self, key):
        return self.list[key]
    # This function allows a value to be obtained from the hash table through subscripting.
    # It has a time complexity of O(1) and a space complexity of O(1).
    def __getitem__(self, key):
        return self.list[key]