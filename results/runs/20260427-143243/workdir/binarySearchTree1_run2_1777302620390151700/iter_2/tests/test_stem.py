from source import BinaryTree
import pytest

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

def test_contains_on_empty_tree():
    tree = BinaryTree()
    assert 5 not in tree

def test_contains_existing_value():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    assert 5 in tree
    assert 3 in tree

def test_contains_nonexistent_value():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    assert 4 not in tree

def test_closest_on_empty_tree():
    tree = BinaryTree()
    assert tree.closest(5) is None

def test_closest_single_value():
    tree = BinaryTree()
    tree.add(5)
    assert tree.closest(5) == 5

def test_closest_with_multiple_values():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.closest(6) in [5, 7]

def test_closest_with_equidistant_values():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.closest(4) in [3, 5]

def test_remove_root_node():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.remove(5)
    assert list(tree) == [3, 7]

def test_add_large_numbers():
    tree = BinaryTree()
    tree.add(10 ** 6)
    tree.add(10 ** 7)
    tree.add(10 ** 8)
    assert list(tree) == [10 ** 6, 10 ** 7, 10 ** 8]

def test_add_negative_numbers():
    tree = BinaryTree()
    tree.add(-5)
    tree.add(-10)
    tree.add(-1)
    assert list(tree) == [-10, -5, -1]

def test_remove_root_with_children():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.remove(10)
    assert list(tree) == [5, 15]

def test_remove_root_with_left_child():
    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(3)
    tree.remove(10)
    assert list(tree) == [3, 5]

def test_closest_with_large_numbers():
    tree = BinaryTree()
    tree.add(100)
    tree.add(200)
    tree.add(300)
    assert tree.closest(250) in [200, 300]

def test_closest_with_negative_numbers():
    tree = BinaryTree()
    tree.add(-10)
    tree.add(-20)
    tree.add(-30)
    assert tree.closest(-25) in [-20, -30]

def test_contains_large_numbers():
    tree = BinaryTree()
    tree.add(1000000)
    tree.add(2000000)
    assert 1000000 in tree
    assert 2000000 in tree
    assert 3000000 not in tree

def test_contains_negative_numbers():
    tree = BinaryTree()
    tree.add(-1)
    tree.add(-2)
    assert -1 in tree
    assert -2 in tree
    assert 0 not in tree

def test_get_min_with_large_numbers():
    tree = BinaryTree()
    tree.add(1000000)
    tree.add(2000000)
    assert tree.getMin() == 1000000

def test_get_max_with_large_numbers():
    tree = BinaryTree()
    tree.add(1000000)
    tree.add(2000000)
    assert tree.getMax() == 2000000

def test_get_min_with_negative_numbers():
    tree = BinaryTree()
    tree.add(-1)
    tree.add(-2)
    assert tree.getMin() == -2

def test_get_max_with_negative_numbers():
    tree = BinaryTree()
    tree.add(-1)
    tree.add(-2)
    assert tree.getMax() == -1

def test_add_with_addition_operator():
    tree = BinaryTree()
    tree.add(1 + 1)
    tree.add(2 + 2)
    assert list(tree) == [2, 4]

def test_add_with_multiplication_operator():
    tree = BinaryTree()
    tree.add(2 * 2)
    tree.add(3 * 3)
    assert list(tree) == [4, 9]

def test_add_with_division_operator():
    tree = BinaryTree()
    tree.add(10 / 2)
    tree.add(15 / 3)
    assert list(tree) == [5.0, 5.0]

def test_add_with_right_shift_operator():
    tree = BinaryTree()
    tree.add(8 >> 1)
    tree.add(16 >> 2)
    assert list(tree) == [4, 4]

def test_add_with_left_shift_operator():
    tree = BinaryTree()
    tree.add(1 << 2)
    tree.add(2 << 3)
    assert list(tree) == [4, 16]

def test_add_with_bitwise_or_operator():
    tree = BinaryTree()
    tree.add(1 | 2)
    tree.add(2 | 3)
    assert list(tree) == [3, 3]

def test_add_with_bitwise_and_operator():
    tree = BinaryTree()
    tree.add(1 & 2)
    tree.add(2 & 3)
    assert list(tree) == [0, 2]