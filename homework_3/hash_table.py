# для разрешения коллизий выбрал Робина Гуда, потому что звучит круто
import pytest

class RobinHoodHashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self._table = [None] * capacity
        self.size = 0
        self.max_load = 0.8

    def _true_index(self, key):
        return hash(key) % self.capacity

    def _grow(self):
        old_sherwood = [tree for tree in self._table if tree is not None]
        self.capacity *= 2
        self._table = [None] * self.capacity
        self.size = 0
        for (key, value, distance) in old_sherwood:
            self.put(key, value)

    def put(self, key, value):
        if self.size > self.capacity * self.max_load:
            self._grow()
        poor_index = self._true_index(key)
        distance = 0
        while True:
            if self._table[poor_index] is None: # мирно занимаем пустую ячейку
                self._table[poor_index] = (key, value, distance)
                self.size += 1
                return
            rich_slot = self._table[poor_index]
            if key == rich_slot[0]: # чуть менее мирно заменяем значение при равных ключах
                self._table[poor_index] = (key, value, distance)
                return
            if distance > rich_slot[2]: # совсем уж воинственно выталкиваем старика
                self._table[poor_index] = (key, value, distance)
                key, value, distance = rich_slot
                # вот тут богатый потерял дом, стал бедным, и Робин Гуд идет помогать уже ему
            distance += 1
            poor_index = (poor_index + 1) % self.capacity

    def get(self, key):
        target_index = self._true_index(key)
        distance = 0
        while True:
            target_slot = self._table[target_index]
            if target_slot is None:
                return None
            if target_slot[0] == key:
                return target_slot[1]
            if distance > target_slot[2]:  # если в нашем слоте сидит кто-то
                return None                # со слишком малой дистанцией, можно не искать дальше
            distance += 1
            target_index = (target_index + 1) % self.capacity

    def remove(self, key):
        evil_index = self._true_index(key)
        distance = 0
        while True:
            evil_slot = self._table[evil_index]
            if evil_slot is None:
                return None
            if evil_slot[0] == key:
                evil_value = evil_slot[1]
                self._execute(evil_index)
                self.size -= 1
                return evil_value
            if distance > evil_slot[2]:
                return None
            distance += 1
            evil_index = (evil_index + 1) % self.capacity

    def _execute(self, evil_index): # избавляться будем с помощью сдвига, чтоб длинные дистанции не копились
        self._table[evil_index] = None
        bad_index = (evil_index + 1) % self.capacity
        while True:
            bad_slot = self._table[bad_index]
            if bad_slot is None:
                return
            if bad_slot[2] == 0:
                return
            good_index = (bad_index - 1) % self.capacity
            bad_slot[2] -= 1
            self._table[good_index] = bad_slot
            self._table[bad_index] = None
            bad_index = (bad_index + 1) % self.capacity

@pytest.fixture
def table():
    return RobinHoodHashTable(capacity=8)

def test_put_get(table):
    table.put("a", 1)
    table.put("b", 2)
    table.put("c", 3)

    assert table.get("a") == 1
    assert table.get("b") == 2
    assert table.get("c") == 3

def test_update_remove(table):
    table.put("x", 10)
    table.put("x", 99)  # обновление значения
    assert table.get("x") == 99
    table.remove("x")
    assert table.get("x") == None


