

hash_table_size = 8

hash_table = [None]  * hash_table_size

def myhash(s):
    str_bytes = s.encode()


    total = 0

    for b in str_bytes:
        total +=b

    return total

def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

def put(key,value):
    # Get the index into the hash table list
    index = hash_index(key)
    hash_table[index] = value

def get(key):

    index = hash_index(key)
    value = hash_table[index]

    return value

def delete(key):

    index = hash_index(key)
    hash_table[index] = None
    

if __name__ == "__main__":
    # if running from command line

    # print(hash_index('Hello'))
    # print(hash_index('foobar'))
    # print(hash_index('cats'))
    # print(hash_index('dork'))
    # print(hash_index('lamb'))

    put("hello",37)
    put("foobar", 128)
    put('cats', "dogs")
    put('foobaz', 168) # collisions with foobar
    print("BEFORE",hash_table)

    delete("hello")
    print("AFTER",hash_table)
