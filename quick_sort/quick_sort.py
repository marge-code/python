import random

def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]
    while i < j:
        while nums[i] <= pivot and i < right:
            i += 1
        while nums[j] > pivot and j > left:
            j -= 1
        if i < j:
            swap(nums, i, j)
    if nums[i] > nums[right]:
        swap(nums, i, right)
    return i

def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1)

def _quick_sort(nums, left, right):
    if left >= right:
        return

    middle = partition(nums, left, right)
    _quick_sort(nums, left, middle - 1)
    _quick_sort(nums, middle + 1, right)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def test():
    empty = []
    quick_sort(empty)
    assert empty == []

    for i in range(1000):
        test_nums = [random.randint(0, 1000) for i in range(1000)]
        sorted_ = sorted(test_nums)
        quick_sort(test_nums)
        assert test_nums == sorted_

if __name__ == '__main__':
    test()
