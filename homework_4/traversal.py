import pytest

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
        else:
            self._recursive_insert(value, self.root)
            self.size += 1

    def _recursive_insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._recursive_insert(value, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._recursive_insert(value, node.right)

    def preorder(self):
        sticks = []
        self._recursive_preorder(self.root, sticks)
        return sticks

    def _recursive_preorder(self, node, sticks):
        if node is not None:
            sticks.append(node.value)
            self._recursive_preorder(node.left, sticks)
            self._recursive_preorder(node.right, sticks)

    def postorder(self):
        sticks = []
        self._recursive_postorder(self.root, sticks)
        return sticks

    def _recursive_postorder(self, node, sticks):
        if node is not None:
            self._recursive_postorder(node.left, sticks)
            self._recursive_postorder(node.right, sticks)
            sticks.append(node.value)

    def inorder(self):
        sticks = []
        self._recursive_inorder(self.root, sticks)
        return sticks

    def _recursive_inorder(self, node, sticks):
        if node is not None:
            self._recursive_inorder(node.left, sticks)
            sticks.append(node.value)
            self._recursive_inorder(node.right, sticks)

    def reverse_preorder(self):
        sticks = []
        self._rec_rev_preorder(self.root, sticks)
        return sticks

    def _rec_rev_preorder(self, node, sticks):
        if node is not None:
            sticks.append(node.value)
            self._rec_rev_preorder(node.right, sticks)
            self._rec_rev_preorder(node.left, sticks)

    def reverse_postorder(self):
        sticks = []
        self._rec_rev_postorder(self.root, sticks)
        return sticks

    def _rec_rev_postorder(self, node, sticks):
        if node is not None:
            self._rec_rev_postorder(node.right, sticks)
            self._rec_rev_postorder(node.left, sticks)
            sticks.append(node.value)

    def reverse_inorder(self):
        sticks = []
        self._rev_rec_inorder(self.root, sticks)
        return sticks

    def _rev_rec_inorder(self, node, sticks):
        if node is not None:
            self._rev_rec_inorder(node.right, sticks)
            sticks.append(node.value)
            self._rev_rec_inorder(node.left, sticks)


def test_preorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.preorder()
    expected = [4, 2, 1, 3, 6, 5, 7]
    assert sticks == expected


def test_postorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.postorder()
    expected = [1, 3, 2, 5, 7, 6, 4]
    assert sticks == expected


def test_inorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.inorder()
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert sticks == expected


def test_reverse_preorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.reverse_preorder()
    expected = [4, 6, 7, 5, 2, 3, 1]
    assert sticks == expected


def test_reverse_postorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.reverse_postorder()
    expected = [7, 5, 6, 3, 1, 2, 4]
    assert sticks == expected


def test_reverse_inorder():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    sticks = bst.reverse_inorder()
    expected = [7, 6, 5, 4, 3, 2, 1]
    assert sticks == expected