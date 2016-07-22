import random

class Heap:
    def __init__(self):
        self.tree = [None]

    @property 
    def size(self):
        return len(self.tree) - 1

    def insert(self, item):
        self.tree.append(item)
        i = self.size
        i_parent = self._get_parent(i)
        while i > 1 and self.tree[i_parent] > self.tree[i]:
            self._swap(i, i_parent)
            i = i_parent
            i_parent = self._get_parent(i)

    def extract_min(self):
        if self.is_empty():
            raise ValueError('Extract from empty heap')
        min_element = self.tree[1]
        self._swap(1, self.size)
        self.tree.pop()
        i = 1
        min_child_i = self._get_min_child(i)
        while min_child_i and self.tree[i] > self.tree[min_child_i]:
            self._swap(i, min_child_i)
            i = min_child_i
            min_child_i = self._get_min_child(i)
        return min_element

    def is_empty(self):
        return self.size < 1

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
            return left if self.tree[left] < self.tree[right] else right

    def _swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def __str__(self):
        return ' '.join(map(str, self.tree[1:]))


def heap_sort(nums):
    h = Heap()
    for num in nums:
        h.insert(num)
    sorted_nums = []
    while not h.is_empty():
        min_element = h.extract_min()
        sorted_nums.append(min_element)
    return sorted_nums

def test():
    for i in range(100):
        test_nums = [random.randint(0, 100) for i in range(1000)]
        assert heap_sort(test_nums) == sorted(test_nums)

if __name__ == "__main__":
    test()