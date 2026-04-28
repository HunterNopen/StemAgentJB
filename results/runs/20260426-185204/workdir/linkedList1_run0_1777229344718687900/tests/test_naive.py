import pytest
from source import SinglyLinkedList, DoublyLinkedList

def test_singly_linked_list_append():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    assert len(sll) == 3
    assert sll[0] == 1
    assert sll[1] == 2
    assert sll[2] == 3

def test_singly_linked_list_get_set():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll[1] = 5
    assert sll[1] == 5
    with pytest.raises(IndexError):
        sll[3]
    with pytest.raises(IndexError):
        sll[-1]

def test_singly_linked_list_contains():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    assert 1 in sll
    assert 2 in sll
    assert 3 not in sll

def test_doubly_linked_list_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert len(dll) == 3
    assert dll[0] == 1
    assert dll[1] == 2
    assert dll[2] == 3

def test_doubly_linked_list_contains():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    assert 1 in dll
    assert 2 in dll
    assert 3 not in dll