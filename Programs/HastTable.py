# Hash Table implementation using list.
HashTableLen = 10
HashTable = [[] for _ in range(HashTableLen)]


def HashF(value):
    return value % HashTableLen

def insert(value):
    hashKey = HashF(value)
    HashTable[hashKey] = (value)

insert(10)
