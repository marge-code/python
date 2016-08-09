def search_rec(nums, key, left, right):
	if left == right:
		return None
	middle = (left + right) / 2
	if key == nums[middle]:
		return middle
	else:
		if key < nums[middle]:
			return search_rec(nums, key, left, middle - 1)
		elif key > nums[middle]:
			return search_rec(nums, key, middle + 1, right)

def search_iter(nums, key):
	left = 0
	right = len(nums) - 1
	while True:
		if left == right:
			break
		middle = (left + right) / 2
		if key == nums[middle]:
			return middle
		elif key < nums[middle]:
			right = middle - 1
		elif key > middle:
			left = middle + 1

nums = [1, 2, 3, 4, 5, 6, 7, 9]

#print search_rec(nums, 100, 0, len(nums))
print search_iter(nums, 100)