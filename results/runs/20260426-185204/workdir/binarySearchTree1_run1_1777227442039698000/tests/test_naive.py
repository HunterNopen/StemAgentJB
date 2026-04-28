import pytest
from source import BinaryTree

def test_add_and_iter():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(3)
    assert list(tree) == [3, 3, 5, 7]

def test_remove():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.remove(3)
    assert list(tree) == [5, 7]
    tree.remove(5)
    assert list(tree) == [7]
    tree.remove(7)
    assert list(tree) == []

def test_remove_nonexistent():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.remove(10)
    assert list(tree) == [3, 5]

def test_get_min():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.getMin() == 3

def test_get_max():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.getMax() == 7

def test_get_min_empty():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMin()

def test_get_max_empty():
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
    assert 10 not in tree

def test_contains_empty():
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

def test_closest_empty():
    tree = BinaryTree()
    assert tree.closest(5) is None

def test_closest_exact_match():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.closest(5) == 5

def test_duplicate_insertion():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(3)
    tree.add(7)
    assert list(tree) == [3, 3, 5, 7]