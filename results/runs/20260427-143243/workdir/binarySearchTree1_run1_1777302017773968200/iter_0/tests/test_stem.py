from source import BinaryTree
import pytest

def test_add_and_inorder_traversal():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(3)
    tree.add(2)
    tree.add(8)
    assert list(tree) == [2, 3, 3, 5, 7, 8]

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
    tree.add(2)
    tree.add(8)
    assert tree.getMin() == 2
    assert tree.getMax() == 8

def test_get_min_and_max_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMin()
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

def test_contains_empty_tree():
    tree = BinaryTree()
    assert 5 not in tree

def test_closest():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(6)
    tree.add(8)
    assert tree.closest(4) == 5
    assert tree.closest(6) == 6
    assert tree.closest(10) == 8
    assert tree.closest(1) == 3

def test_closest_empty_tree():
    tree = BinaryTree()
    assert tree.closest(5) is None

def test_add_duplicates():
    tree = BinaryTree()
    tree.add(5)
    tree.add(5)
    tree.add(5)
    assert list(tree) == [5, 5, 5]

def test_remove_duplicates():
    tree = BinaryTree()
    tree.add(5)
    tree.add(5)
    tree.add(5)
    tree.remove(5)
    assert list(tree) == [5, 5]

def test_remove_all_duplicates():
    tree = BinaryTree()
    tree.add(5)
    tree.add(5)
    tree.add(5)
    tree.remove(5)
    tree.remove(5)
    tree.remove(5)
    assert list(tree) == []

def test_edge_case_closest_with_multiple_equidistant():
    tree = BinaryTree()
    tree.add(1)
    tree.add(3)
    tree.add(5)
    assert tree.closest(4) in {3, 5}

def test_edge_case_closest_with_negative():
    tree = BinaryTree()
    tree.add(-10)
    tree.add(-5)
    tree.add(0)
    assert tree.closest(-7) == -5

def test_edge_case_closest_with_large_numbers():
    tree = BinaryTree()
    tree.add(1000000)
    tree.add(5000000)
    tree.add(10000000)
    assert tree.closest(7500000) == 5000000

def test_remove_root_node():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.remove(5)
    assert list(tree) == [3, 7]