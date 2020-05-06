class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        #next is only for collisions
        self.next = None


    def __repr__(self):
        return f"{self.key}--{self.value}--next:{self.next}"



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = 0):
        self.capacity = capacity
        self.storage = [None] * capacity




    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        hash = 5381

        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity


        return self.djb2(key) % self.capacity



    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        index = self.hash_index(key)
        new_node = HashTableEntry(key,value)

        if self.storage[index] is not None:
            node = self.storage[index]
            if node.key == key:
                node.value = value
                return f"inserted new value:{value}"
            else:
                while node.next is not None:
                    node = node.next
                    if node.key == key:
                        node.value = value
                        return f"inserted new value:{value}"

                node.next = new_node

                return f"inserted new value:{value} in linked list"

        else:
            self.storage[index] = new_node
            return f"inserted value:{value} at beginning of list"


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
       

        if self.storage[index] is not None:
            node = self.storage[index]
            if key == node.key:
                node.key = None
            else:
                while node.next is not None:
                    node = node.next

                    if key == node.key:
                        node.key = None
                        
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
       

        if self.storage[index] is not None:
            node = self.storage[index]
            # print(f"initial node{node}")

            if key == node.key:
                return node.value
            else:
                while node.next is not None:
                    node = node.next
                    # print(f'comparison{key}=={node.key}')
                    if key == node.key:
                        return node.value 
                        
        return None
            


    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

# ht = HashTable(8)

# ht.put("key-0", "val-0")
# ht.put("key-1", "val-1")
# ht.put("key-2", "val-2")
# ht.put("key-3", "val-3")
# ht.put("key-4", "val-4")
# ht.put("key-5", "val-5")
# ht.put("key-6", "val-6")
# ht.put("key-7", "val-7")
# ht.put("key-8", "val-8")
# ht.put("key-9", "val-9")

# for g in ht.storage:
#     print(g)

# print("get:",ht.get("key-8"))

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.put("line_1", "Tiny hash table")
#     ht.put("line_2", "Filled beyond capacity")
#     ht.put("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.get("line_1"))
#     print(ht.get("line_2"))
#     print(ht.get("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.get("line_1"))
#     print(ht.get("line_2"))
#     print(ht.get("line_3"))

#     print("")
