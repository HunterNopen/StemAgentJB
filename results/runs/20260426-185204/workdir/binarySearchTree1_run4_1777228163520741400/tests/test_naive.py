import pytest
from source import BinaryTree

def test_initialization():
    tree = BinaryTree()
    assert tree.root is None

def test_add_single_value():
    tree = BinaryTree()
    tree.add(10)
    assert tree.root.value == 10
    assert tree.root.left is None
    assert tree.root.right is None

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
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert 10 in tree
    assert 5 in tree
    assert 15 in tree
    assert 20 not in tree

def test_contains_empty_tree():
    tree = BinaryTree()
    assert 10 not in tree

def test_remove_leaf_node():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(5)
    assert 5 not in tree
    assert tree.root.left is None

def test_remove_node_with_one_child():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    tree.remove(15)
    assert 15 not in tree
    assert tree.root.right.value == 12

def test_remove_node_with_two_children():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    tree.add(18)
    tree.remove(15)
    assert 15 not in tree
    assert tree.root.right.value == 12
    assert tree.root.right.right.value == 18

def test_remove_non_existent_value():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(20)
    assert 10 in tree
    assert 5 in tree
    assert 15 in tree

def test_closest_on_empty_tree():
    tree = BinaryTree()
    assert tree.closest(10) is None

def test_closest_on_single_node_tree():
    tree = BinaryTree()
    tree.add(10)
    assert tree.closest(10) == 10
    assert tree.closest(8) == 10
    assert tree.closest(12) == 10

def test_closest_on_multiple_nodes():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    assert tree.closest(11) == 10
    assert tree.closest(14) == 15
    assert tree.closest(6) == 5

def test_iter():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    assert list(iter(tree)) == [5, 10, 12, 15]