import random

class HashTable:

    DEFAULT_SIZE = 19
    GROWTH_FACTOR = 2
    MAX_LOAD_FACTOR = 3

    def __init__(self):
        self.items_count = 0
        self.table = self._allocate_buckets(self.DEFAULT_SIZE)
        self.version = 0


    def insert(self, key, value):
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(self.table[bucket]):
            if k == key:
                    self.table[bucket][i] = (key, value)
                    return
        self.table[bucket].append( (key, value) )
        self.items_count += 1
        if self._overcrowded():
            self._rehash()

    
    def search(self, key):
        bucket = self._get_bucket(key)
        for (k, v) in self.table[bucket]:
            if k == key:
                return v
        return None


    def delete(self, key):
        bucket = self._get_bucket(key)
        for (k, v) in self.table[bucket]:
            if k == key:
                self.table[bucket].remove( (k, v) )
                return True
        raise KeyError('HashTable.delete(key): {} not in HashTable'.format(key))


    def _get_bucket(self, key):
        return hash(key) % len(self.table)

    
    def _overcrowded(self):
        return self._get_load_factor() > self.MAX_LOAD_FACTOR


    def _get_load_factor(self):
        return float(self.items_count) / len(self.table)
        
    
    def _rehash(self):
        new_table_num_buckets = len(self.table) * self.GROWTH_FACTOR
        new_table = self._allocate_buckets(new_table_num_buckets)
        all_items = []
        for bucket in self.table:
            all_items.extend(bucket)
        self.table = new_table
        for (k, v) in all_items:
            self.insert(k, v)
        self.version += 1


    def _allocate_buckets(self, num_buckets):
        return [[] for x in range(num_buckets)]

    
    def print_table(self):
        for bucket in self.table:
            print bucket


    def __str__(self):
        return str(self.table)


    def __contains__(self, key):
        value = self.search(key)
        return value is not None


    def __getitem__(self, key):
        value = self.search(key)
        if value is None:
            raise KeyError("key not found: {}".format(key))
        return value

    def __len__(self):
        return self.items_count

    def __iter__(self):
        print "iterator requested"
        return HashTableIterator(self.table, self.version)



class HashTableIterator:
    __next__ = next

    def __init__(self, table, version):
        self.table = table
        self.current_bucket = 0
        self.current_item = 0

    def __iter__(self):
        return self

    def next(self):
        for i in range(self.current_bucket, len(self.table)):
            if self.table[i] and len(self.table[i]) > self.current_item:
                self.current_bucket = i
                next_key = self.table[i][self.current_item][0]
                self.current_item += 1
                return next_key
            self.current_item = 0
        raise StopIteration

def test():
    h = HashTable()
    for item in range(100):
        h.insert(item, random.randint(1, 100))
    assert (1 in h) == True
    assert h.delete(2) == True
    assert h.search(2) == None
    assert h[5] == h.search(5)


if __name__ == '__main__':
    test()
