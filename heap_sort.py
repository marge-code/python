class Heap:
	def __init__(self):
		tree = [None]
		self.tree = tree
		size = len(self.tree) - 1
		self.size = size

	def insert(self, x):
		self.tree.append(x)
		i = len(self.tree) - 1
		while i >= 1 and self.tree[i / 2] > self.tree[i]:
			self._swap(self.tree, i / 2, i)
			i /= 2
		self.size = len(self.tree) - 1

	def _swap(self, tree, i, j):
		tree[i], tree[j] = tree[j], tree[i]

	def extract_min(self):
		min_el = self.tree[1]
		print 'min: {}'.format(self.tree[1])
		size = self.size
		self._swap(self.tree, 1, size)
		self.size -= 1
		i = 1
		min_child_index = self._get_min_child_index(i, self.size)
		while min_child_index and self.tree[i] > self.tree[min_child_index]:
			self._swap(self.tree, i, min_child_index)
			i = min_child_index
			min_child_index = self._get_min_child_index(i, self.size)
			
	def _get_min_child_index(self, i, size):
		left = i * 2
		right = i * 2 + 1
		if left > size:
			return None
		elif right > size:
			return left
		else:
			return left if self.tree[left] <= self.tree[right] else right
		
	def __str__(self):
		return str(self.tree)


def heap_sort(nums):
	h = Heap()
	for num in nums:
		h.insert(num)
	while h.size:
		h.extract_min()
	print h
