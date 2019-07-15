class HashTable(object):
    def __init__(self):
        self.size = 11
        self.data = [None] * self.size
        self.slots = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunc(key,len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[hashvalue] != key:
                    nextslot =  self.rehash(hashvalue,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data


    def get (self,key):
        startslot = self.hashfunc(key,len(self.slots))
        data = None
        stop = None
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop  = True
        return data

            
    def hashfunc(self,key,size):
        return key % size

    def rehash(self,key,size):
        return (key+1)%size

    def __setitem__(self,key,data):
        self.put(key,data)

    def __getitem__(self,key):
        return self.get(key)



h = HashTable()
h[11] = 'books'
h[52] = 'my books2'
h[53] = 'my book3'
h[54] = 'my book4'
h[11] = 'my book1'
h[56] = 'my book6'
h[20] = 'sunny'
h[20] = 'sunny'


