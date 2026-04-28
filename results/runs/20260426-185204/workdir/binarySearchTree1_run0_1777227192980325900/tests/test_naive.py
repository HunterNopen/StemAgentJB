import pytest
from source import BinaryTree

def test_add_and_inorder_traversal():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    assert list(tree) == [2, 3, 4, 5, 6, 7, 8]

def test_add_duplicates():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    assert list(tree) == [2, 3, 4, 5, 5]

def test_remove_leaf_node():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.remove(3)
    assert list(tree) == [5, 7]

def test_remove_node_with_one_child():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(6)
    tree.remove(7)
    assert list(tree) == [3, 5, 6]

def test_remove_node_with_two_children():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(6)
    tree.add(8)
    tree.remove(7)
    assert list(tree) == [3, 5, 6, 8]

def test_remove_nonexistent_value():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.remove(10)
    assert list(tree) == [3, 5, 7]

def test_get_min_and_max():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.getMin() == 3
    assert tree.getMax() == 7

def test_get_min_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMin()

def test_get_max_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMax()

def test_contains():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert 5 in tree
    assert 3 in tree
    assert 7 in tree
    assert 4 not in tree

def test_contains_empty_tree():
    tree = BinaryTree()
    assert 5 not in tree

def test_closest():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.closest(4) == 5
    assert tree.closest(6) == 5
    assert tree.closest(8) == 7

def test_closest_empty_tree():
    tree = BinaryTree()
    assert tree.closest(4) is None