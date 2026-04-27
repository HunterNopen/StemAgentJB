from source import BinaryTree
import pytest

def test_add_and_inorder_traversal():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(3)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)
    assert list(tree) == [2, 3, 3, 4, 5, 6, 7, 8]

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
    assert tree.closest(4) == 5
    assert tree.closest(6) == 5
    assert tree.closest(10) == 7
    assert tree.closest(1) == 3

def test_closest_empty_tree():
    tree = BinaryTree()
    assert tree.closest(5) is None

def test_closest_multiple_equidistant():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    assert tree.closest(6) in {5, 7}

def test_performance_large_tree():
    tree = BinaryTree()
    for i in range(1000):
        tree.add(i % 10)
    assert len(list(tree)) == 1000

def test_remove_all_elements():
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    for i in range(10):
        tree.remove(i)
    assert list(tree) == []

def test_remove_root_node():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(10)
    assert list(tree) == [5, 15]

def test_remove_root_with_children():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(12)
    tree.remove(10)
    assert list(tree) == [5, 12, 15]

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

def test_remove_nonexistent_duplicates():
    tree = BinaryTree()
    tree.add(5)
    tree.add(5)
    tree.add(5)
    tree.remove(10)
    assert list(tree) == [5, 5, 5]

def test_repr_empty_tree():
    tree = BinaryTree()
    assert repr(tree) == 'binary:()'

def test_repr_non_empty_tree():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    assert repr(tree) != 'binary:()'

def test_add_with_greater_than_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert list(tree) == [5, 10, 15]

def test_remove_with_greater_than_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(15)
    assert list(tree) == [5, 10]

def test_closest_with_greater_than_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(12) == 10

def test_remove_root_with_greater_than_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(10)
    assert list(tree) == [5, 15]

def test_add_and_remove_with_not_equal_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(5)
    assert 5 not in tree

def test_closest_with_not_equal_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(6) == 5

def test_add_and_remove_with_subtraction_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert len(list(tree)) == 3
    tree.remove(5)
    assert len(list(tree)) == 2

def test_closest_with_subtraction_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(8) == 10

def test_add_and_remove_with_addition_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert len(list(tree)) == 3
    tree.add(20)
    assert len(list(tree)) == 4

def test_closest_with_addition_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(14) == 15

def test_remove_with_bitwise_or_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(10)
    assert 10 not in tree

def test_closest_with_bitwise_or_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(11) == 10

def test_remove_with_bitwise_xor_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(15)
    assert 15 not in tree

def test_closest_with_bitwise_xor_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(16) == 15

def test_remove_with_left_shift_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(5)
    assert 5 not in tree

def test_closest_with_left_shift_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(4) == 5

def test_remove_with_right_shift_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(15)
    assert 15 not in tree

def test_closest_with_right_shift_operator():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.closest(16) == 15