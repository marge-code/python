class Heap:
    def __init__(self):
        self.tree = [None]

    @property 
    def size(self):
        return len(self.tree) - 1

    def insert(self, item):
        self.tree.append(item)
        i = len(self.tree) - 1
        while i > 1 and self.tree[self._get_parent(i)] > self.tree[i]:
            self._swap(i, self._get_parent(i))
            i = self._get_parent(i)

    def extract_min(self):
        min_el = self.tree[1]
        self._swap(1, self.size)
        self.tree.pop(self.size)
        i = 1
        min_child = self._get_min_child(i)
        while min_child and self.tree[i] > self.tree[min_child]:
            self._swap(i, self._get_min_child(i))
            i = min_child
            min_child = self._get_min_child(i)
        return min_el


    def _get_parent(self, i):
        return i / 2

    def _get_left(self, i):
        return i * 2

    def _get_right(self, i):
        return i * 2 + 1

    def _get_min_child(self, i):
        left = self._get_left(i)
        right = self._get_right(i)
        if left > self.size:
            return None
        elif right > self.size:
            return left
        else:
            return min(left, right)

    def _swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def __str__(self):
        return ' '.join(map(str, self.tree))


def heap_sort(nums):
	h = Heap()
	for num in nums:
		h.insert(num)
	while h.size:
		h.extract_min()
	print h
