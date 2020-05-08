import random
import sys
sys.setrecursionlimit(10000)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    traverse = words.split()

# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences

class HashTableEntry:

    def __init__(self,key, value):
        self.key = key
        self.value = value
        #next is only for collisions
        self.next = None

    def __repr__(self):
        return f"${self.value}--next:{self.next}"


cache = {}


def insert():
    for x in range(0, len(traverse[0:400])):
        for y in range(0, len(traverse)-1):
            if traverse[y].lower() == traverse[x].lower():
                if traverse[x] not in cache:
                    cache[traverse[x]] = HashTableEntry(traverse[x], traverse[y+1])
                else:
                    node = cache[traverse[x]]
                    
                    if node.key == traverse[x] and node.value == traverse[y+1]:
                        node.value = traverse[y+1]
                    else:
                        node = cache[traverse[x]]
                        while node.next is not None:
                            node = node.next

                            if node.key == traverse[x] and node.value == traverse[y+1]:
                                node.value = traverse[y+1]
                                        

                        node.next = HashTableEntry(traverse[x],traverse[y+1])

    print(cache)

            

insert()
