import pytest
from traversal import BinarySearchTree, TreeNode

def is_bst(root):
    def validator(node, minim, maxim):
        if node is None:
            return True

        if node.value < minim or node.value >= maxim:
            return False

        return validator(node.left, minim, node.value) and validator(node.right, node.value, maxim)

    return validator(root, -float('inf'), float('inf'))

def test_is_bst():
    bst = BinarySearchTree()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for value in values:
        bst.insert(value)
    assert is_bst(bst.root) is True

def test_is_not_bst():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(17)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(11) # не может быть в левом поддереве корня
    assert is_bst(root) is False

def test_empty_tree():
    assert is_bst(None) == True

def test_single_tree():
    assert is_bst(TreeNode(10)) == True

def test_r_duplicate_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(5) # дубликат справа - норм
    assert is_bst(root) is True

def test_l_duplicate_tree():
    root = TreeNode(5)
    root.left = TreeNode(5) # дубликат слева - норм
    root.right = TreeNode(3)
    assert is_bst(root) is False
