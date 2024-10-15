# Payal Chavan
# CS 5800 Algorithms (Seattle)
# Summer 2024
# Assignment 9
# Program for implementing HashMap
# Date: 08/16/2024



class HashMap:
    # Initialize the hash map with a given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        self.is_testing = False

    # Create a list of empty dictionaries (buckets) for the hash table
    def create_buckets(self):
        return [{} for _ in range(self.size)]

    # Custom hash function to calculate the hash value of a key
    def _hash(self, key):
        # return hash(key) % self.size
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.size
        return hash_value

    # Insert a key-value pair into the hash map
    def insert(self, key, value):
        if not self.is_testing:
            print(f"Insert: {key}: {value}")
        address = self._hash(key)
        if key in self.hash_table[address]:
            self.hash_table[address][key] = value
        else:
            self.hash_table[address][key] = value

    # Lookup a value by its key in the hash map
    def lookup(self, key):
        if not self.is_testing:
            print(f"Lookup: {key}")
        address = self._hash(key)
        if key in self.hash_table[address]:
            return self.hash_table[address][key]
        return "Data Not Found"

    # Delete a key-value pair from the hash map
    def delete(self, key):
        if not self.is_testing:
            print(f"Delete: {key}")
        address = self._hash(key)
        if key in self.hash_table[address]:
            del self.hash_table[address][key]

    # Traverse and print all key-value pairs in the hash map
    def traverse(self):
        for bucket in self.hash_table:
            for key, value in bucket.items():
                print(f"Key: {key}, Value: {value}")


# Performance Testing
'''
This code will create a graph showing the performance of insert, delete, and lookup operations as the number of elements increases. 
You can adjust the sizes list to test with different numbers of elements.
'''


def performance_test():
    import time
    import matplotlib.pyplot as plt

    sizes = [10, 100, 1000, 10000, 100000]
    insert_times = []
    delete_times = []
    lookup_times = []

    for size in sizes:
        hash_map = HashMap(size)
        hash_map.is_testing = True

        keys = [f'key{i}' for i in range(size)]
        values = [i for i in range(size)]

        # Measure insert time
        start_time = time.time()
        for key, value in zip(keys, values):
            hash_map.insert(key, value)
        insert_times.append(time.time() - start_time)

        # Measure lookup time
        start_time = time.time()
        for key in keys:
            hash_map.lookup(key)
        lookup_times.append(time.time() - start_time)

        # Measure delete time
        start_time = time.time()
        for key in keys:
            hash_map.delete(key)
        delete_times.append(time.time() - start_time)

    # Plot the performance results
    plt.plot(sizes, insert_times, label='Insert')
    plt.plot(sizes, lookup_times, label='Lookup')
    plt.plot(sizes, delete_times, label='Delete')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('HashMap Performance')
    plt.show()



if __name__ == '__main__':
    # Create a hash map and perform some operations
    hash_map = HashMap(10)
    hash_map.insert("john", 11)
    hash_map.insert("peter", 22)
    hash_map.insert("carrie", 33)
    hash_map.insert("sara", 44)
    hash_map.insert("emily", 55)
    hash_map.insert("mark", 66)
    hash_map.insert("david", 77)
    hash_map.insert("tim", 88)
    hash_map.insert("rose", 99)
    hash_map.insert("lily", 100)
    hash_map.traverse()
    hash_map.insert("carrie", 14)
    hash_map.insert("peter", 99)
    print(hash_map.lookup("john"))
    print(hash_map.lookup("guava")) # Output: Data Not Found
    hash_map.delete("john")
    hash_map.delete("mark")
    hash_map.delete("lily")
    hash_map.delete("david")
    hash_map.traverse()

    # Run performance tests
    performance_test()
