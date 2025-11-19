import time
import random
import pytest

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n  // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(me, ow):
    meow = []
    i = j = 0
    while i < len(me) and j < len(ow):
        if me[i] < ow[j]:
            meow.append(me[i])
            i += 1
        else:
            meow.append(ow[j])
            j += 1
    meow += me[i:]
    meow += ow[j:]

    return meow

def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    guard = arr[n//2]
    left = [guest for guest in arr if guest < guard]
    mid = [guest for guest in arr if guest == guard]
    right = [guest for guest in arr if guest > guard]
    return quicksort(left) + mid + quicksort(right)

# чтобы таймер с ума не сошел, заводим его под отдельные функции

@timer
def quicksort_with_clocks(arr):
    return quicksort(arr)

@timer
def mergesort_with_clocks(arr):
    return mergesort(arr)


@pytest.fixture
def test_arrays():
    arrays = []
    random.seed(463)

    for i in range(10):
        arr = [random.randint(1, 1000) for _ in range(100)]
        arrays.append(arr)

    return arrays

def test_sort(test_arrays):
    for i, arr in enumerate(test_arrays):
        expected = sorted(arr)
        merge_result = mergesort_with_clocks(arr.copy())
        assert merge_result == expected
        quick_result = quicksort_with_clocks(arr.copy())
        assert quick_result == expected

# на тестах quicksort заметно быстрее, хотя мы не рассматриваем краевые случаи