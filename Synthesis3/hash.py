# Payal Chavan
# Summer 2024 
# Algorithms CS 5800
# Synthesis3 - Hash Table
# Date: 08/09/2024




class HashTable:
    # Initialize a hash table with a specified size (default is 10).
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # Private method to compute the hash value for a given key.
        return hash(key) % self.size

    #  Insert a key-value pair into the hash table.
    def insert(self, key, value):
        index = self._hash(key)
        self.buckets[index].append((key, value))

    # Retrieve the value associated with the given key from the hash table.
    def get(self, key):
        print(f"Retrieving value for {key}")
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None


    # Delete a key-value pair from the hash table if the key exists.
    def delete(self, key):
        print(f"Deleting {key}...")
        index = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return


    # Update the value of a key in the hash table if the key exists.
    def update(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                print(f"Update: {key} with {value}")
                self.buckets[index][i] = (key, value)
                return


    # Return all key-value pairs stored in the hash table.
    def get_all(self):
        return [pair for bucket in self.buckets for pair in bucket]

# Execute the main function to test the code.
if __name__ == '__main__':
    my_hash_table = HashTable()
    my_hash_table.insert("apple", 3)
    my_hash_table.insert("banana", 2)
    my_hash_table.insert("cherry", 5)
    my_hash_table.insert("grape", 4)
    my_hash_table.insert("melon", 6)
    my_hash_table.insert("kiwi", 7)

    # Get all key-value pairs
    print("All Key-Value pairs in HashTable")
    kv_pair = my_hash_table.get_all()
    for key, val in kv_pair:
        print(f"{key} \t {val}")
    print()

    print("Key: melon \t Value: ", my_hash_table.get("melon"), "\n")

    my_hash_table.update("kiwi", 15)
    print("Key: kiwi \t Updated Value: ", my_hash_table.get("kiwi"), "\n")

    my_hash_table.delete("grape")
    print("Key: grape \t Value: ", my_hash_table.get("grape"), "\n")

    # Get all key-value pairs
    print("All Key-Value pairs in HashTable")
    kv_pair = my_hash_table.get_all()
    for key, val in kv_pair:
        print(f"{key} \t {val}")
    print()





'''
Output:

All Key-Value pairs in HashTable
apple    3
cherry   5
banana   2
grape    4
melon    6
kiwi     7

Retrieving value for melon
Key: melon       Value:  6 

Update: kiwi with 15
Retrieving value for kiwi
Key: kiwi        Updated Value:  15 

Deleting grape...
Retrieving value for grape
Key: grape       Value:  None 

All Key-Value pairs in HashTable
apple    3
cherry   5
banana   2
melon    6
kiwi     15
'''