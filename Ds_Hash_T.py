''' Hash Table '''

def get_hash(key):
    h = 0 
    for char in key:
        h += ord(char)
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.Max)]
    
    def get_hash(sekf,key):
        h = 0 
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self,key,val):
        h = self.get_hash(key)
        sefl.arr[h] = val
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
            if not found:
                self.arr[h].append((key,val))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        

