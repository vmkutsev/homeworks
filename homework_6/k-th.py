import pytest

def quickselect(big_arr, k):
    rank = len(big_arr) - k
    def select(arr, rank):
        if len(arr) == 1:
            return arr[0]

        guard = arr[len(arr) // 2]
        left = [guest for guest in arr if guest < guard]
        if rank < len(left):
            return select(left, rank)
        mid = [guest for guest in arr if guest == guard]
        if rank < len(left) + len(mid):
            return guard
        right = [guest for guest in arr if guest > guard]

        return select(right, rank - len(left) - len(mid))

    return select(big_arr, rank)

def test_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert quickselect(nums, k) == 5

def test_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert quickselect(nums, k) == 4

def test_3():
    nums = [10, 30, 20, 40, 50]
    assert quickselect(nums, 1) == 50
    assert quickselect(nums, 2) == 40
    assert quickselect(nums, 5) == 10

def test_4():
    nums = [7, 7, 7, 7]
    assert quickselect(nums, 1) == 7
    assert quickselect(nums, 4) == 7