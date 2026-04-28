import pytest
from source import BinaryTree

def test_initial_tree_is_empty():
    tree = BinaryTree()
    assert tree.root is None

def test_add_single_value():
    tree = BinaryTree()
    tree.add(10)
    assert tree.root.value == 10
    assert tree.root.left is None
    assert tree.root.right is None

def test_add_multiple_values():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

def test_add_duplicates():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(5)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.left.left is not None

def test_remove_leaf_node():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.remove(5)
    assert tree.root.left is None

def test_remove_node_with_one_child():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    tree.remove(15)
    assert tree.root.right.value == 12
    assert tree.root.right.right is None

def test_remove_node_with_two_children():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    tree.add(18)
    tree.remove(15)
    assert tree.root.right.value == 12
    assert tree.root.right.right.value == 18

def test_get_min_on_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMin()

def test_get_max_on_empty_tree():
    tree = BinaryTree()
    with pytest.raises(ValueError):
        tree.getMax()

def test_get_min():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.getMin() == 5

def test_get_max():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.getMax() == 15

def test_contains_on_empty_tree():
    tree = BinaryTree()
    assert 10 not in tree

def test_contains_existing_value():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    assert 10 in tree
    assert 5 in tree

def test_contains_non_existing_value():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    assert 15 not in tree

def test_closest_on_empty_tree():
    tree = BinaryTree()
    assert tree.closest(10) is None

def test_closest_value():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(12) == 10
    assert tree.closest(6) == 5
    assert tree.closest(15) == 15

def test_iterate_tree():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert list(tree) == [5, 10, 15]

def test_iterate_tree_with_duplicates():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(5)
    tree.add(15)
    assert list(tree) == [5, 5, 10, 15]