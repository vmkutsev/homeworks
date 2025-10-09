import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linker(list):
    head = Node(list[0])
    current = head
    for item in list[1:]:
        item = Node(item)
        current.next = item
        current = item
    return head

def lister(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

def dummy_merger(l1, l2):
    f = linker(l1)
    s = linker(l2)
    dummy = Node(0)
    current = dummy
    while f and s:
        if f.data > s.data:
            current.next = s
            s = s.next
        else:
            current.next = f
            f = f.next
        current = current.next
    current.next = f if f else s
    return dummy.next

def non_dummy_merger(l1, l2):
    f = linker(l1)
    s = linker(l2)
    if f.data > s.data:
        head = s
        s = s.next
    else:
        head = f
        f = f.next
    current = head
    while f and s:
        if f.data > s.data:
            current.next = s
            s = s.next
        else:
            current.next = f
            f = f.next
        current = current.next
    current.next = f if f else s
    return head

@pytest.mark.parametrize(
    'l1, l2, merged',
    [
        ([1, 2, 4], [1, 3, 4], [1,1,2,3,4,4]),
        ([2, 4, 6], [1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
    ]
)
def test_merge(l1, l2, merged):
    assert lister(dummy_merger(l1, l2)) == merged
    assert lister(non_dummy_merger(l1, l2)) == merged
