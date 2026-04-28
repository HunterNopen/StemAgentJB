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

def test_singly_linked_list_getitem():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    assert sll[1] == 20
    with pytest.raises(IndexError):
        sll[3]
    with pytest.raises(IndexError):
        sll[-1]

def test_singly_linked_list_setitem():
    sll = SinglyLinkedList()
    sll.append(5)
    sll.append(15)
    sll[1] = 25
    assert sll[1] == 25
    with pytest.raises(IndexError):
        sll[2] = 30
    with pytest.raises(IndexError):
        sll[-1] = 40

def test_singly_linked_list_contains():
    sll = SinglyLinkedList()
    a = object()
    b = object()
    sll.append(a)
    sll.append(b)
    assert a in sll
    assert b in sll
    assert object() not in sll

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
    a = object()
    b = object()
    dll.append(a)
    dll.append(b)
    assert a in dll
    assert b in dll
    assert object() not in dll