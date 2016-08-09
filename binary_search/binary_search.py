import random

def binary_search(nums, key):
    return _binary_search_impl(nums, key, 0, len(nums))

def _binary_search_impl(nums, key, left, right):
    if left > right:
        return None

    while left < right:
        middle  = (left + right) / 2
        if nums[middle] == key:
            return middle
        elif key < nums[middle]:
            right = middle
        elif key > nums[middle]:
            left = middle + 1

    return None

def test():
    print ':)'
    assert binary_search([], key=5) == None
    assert binary_search([1], key=5) == None
    assert binary_search([1, 2, 3], key=4) == None
    assert binary_search([1, 2], key=1) == 0
    assert binary_search([1, 2], key=2) == 1
    assert binary_search([1,2,3,4,5], key=5) == 4
    assert binary_search([1,2,3,4,5], key=1) == 0
    test_nums = range(100)
    key = random.randint(0, 99)
    assert binary_search(test_nums, key) == test_nums.index(key)

if __name__ == '__main__':
    test()
