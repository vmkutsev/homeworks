class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        newcomer = Node(data)
        newcomer.next = self.top
        self.top = newcomer
        self.size += 1
    def pop(self):
        if self.top is None:
            return None
        lastcomer = self.top
        self.top = lastcomer.next
        self.size -= 1
        return lastcomer.data

class Queue:
    def __init__(self):
        self.front = None
        self.size = 0
        self.last = None
    def enqueue(self, data):
        newcomer = Node(data)
        if self.last is not None:
            self.last.next = newcomer
        if self.front is None:
            self.front = newcomer
        self.last = newcomer
        self.size += 1
    def dequeue(self):
        if self.front is None:
            return None
        oldcomer = self.front
        self.front = oldcomer.next
        self.size -= 1
        return oldcomer.data

def test_stack():
    s = Stack()
    s.push('a')
    assert s.size == 1
    assert s.top.data == 'a'

    s.push('b')
    assert s.size == 2
    assert s.top.data == 'b'
    assert s.top.next.data == 'a'

    popped = s.pop()
    assert popped == 'b'
    assert s.size == 1
    assert s.top.data == 'a'

    popped = s.pop()
    assert popped == 'a'
    assert s.size == 0
    assert s.top is None

def test_queue_enqueue_dequeue_peek_size_and_empty():
    q = Queue()
    assert q.size == 0

    q.enqueue('a')
    assert q.size == 1
    assert q.front.data == 'a'
    assert q.last.data == 'a'

    q.enqueue('b')
    assert q.size == 2
    assert q.last.data == 'b'
    assert q.front.data == 'a'
    assert q.front.next.data == 'b'

    old = q.dequeue()
    assert old == 'a'
    assert q.size == 1
    assert q.front.data == 'b'

    old = q.dequeue()
    assert old == 'b'
    assert q.size == 0
    assert q.front is None
    assert q.front is None