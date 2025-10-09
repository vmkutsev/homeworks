from stack_vs_queue import Stack
import pytest

def validator(pushed, popped):
    pushed = pushed.split()
    popped = popped.split()
    i = 0
    s = Stack()
    for item in pushed:
        s.push(item)
        while s.top is not None and s.top.data == popped[i]:
            s.pop()
            i += 1
    return s.size == 0


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ('1 2 3 4 5', '1 3 5 4 2', True), # из условия
        ('1 2 3', '3 1 2', False), # тоже
        ('1', '1', True), # один элемент
        ('1 2', '1 2', True), # два
        ('1 2', '2 1', True), # отзеркалим
        ('1 2 3 4 5 6 7', '2 1 4 3 6 5 7', True), # попарно отзеркалены
        ('1 2 3 4 5', '3 1 2 5 4', False) # после тройки и перед единицей надо вытащить двойку
    ]
)
def test_validator(pushed, popped, expected):
    assert validator(pushed, popped) == expected
