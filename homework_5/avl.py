import pytest

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
class AVL:
    def __init__(self):
        self.root = None
    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value(node.right)
                node.value = temp.value
                node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _balance(self, node):
        balance = self._get_balance(node)

        # Left Left
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Right Right
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Left Right
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, x):
        y = x.right
        z = y.left

        y.left = x
        x.right = z

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        z = x.right

        x.right = y
        y.left = z

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node


def test_avl():
    avl = AVL()

    # Сажаем дерево
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(3)
    avl.insert(7)
    avl.insert(12)
    avl.insert(17)

    # Удаляем лист
    avl.delete(3)
    assert avl.search(3) == False
    assert avl.search(5) == True

    # Удаляем узел с одним потомком
    avl.delete(15)
    assert avl.search(15) == False
    assert avl.search(12) == True
    assert avl.search(17) == True

    # Удаляем корень
    avl.delete(10)
    assert avl.search(10) == False
    assert avl.search(5) == True
    assert avl.search(7) == True