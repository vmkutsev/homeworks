import pytest
from traversal import BinarySearchTree, TreeNode

def is_balanced(root):
    def checker(node):
        if node is None:
            return True, 0
        left_checker, left_counter = checker(node.left)
        right_checker, right_counter = checker(node.right)

        actual_counter = max(left_counter, right_counter) + 1
        actual_checker = (left_checker and right_checker and abs(left_counter - right_counter) <= 1)

        return actual_checker, actual_counter

    final_checker, final_counter = checker(root)

    return final_checker

def test_is_balanced():
    bst = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    for value in values:
        bst.insert(value)

    assert is_balanced(bst.root) == True

def test_is_not_balanced_r():
    bst = BinarySearchTree()
    values = [1, 2, 3, 4]
    for value in values:
        bst.insert(value)

    assert is_balanced(bst.root) == False

def test_is_not_balanced_l():
    bst = BinarySearchTree()
    values = [4, 3, 2, 1]
    for value in values:
        bst.insert(value)

    assert is_balanced(bst.root) == False

def test_almost_balanced():
    bst = BinarySearchTree()
    values = [8, 4, 12, 2, 6, 10, 1, 5, 7, 0]
    for value in values:
        bst.insert(value)

    assert is_balanced(bst.root) == False

def test_almost_not_balanced():
    bst = BinarySearchTree()
    values = [8, 4, 12, 2, 6, 10, 1, 5, 7]
    for value in values:
        bst.insert(value)

    assert is_balanced(bst.root) == True
