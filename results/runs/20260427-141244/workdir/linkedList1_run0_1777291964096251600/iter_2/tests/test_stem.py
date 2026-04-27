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
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll[1] = 25
    assert sll[1] == 25
    with pytest.raises(IndexError):
        sll[3]
    with pytest.raises(IndexError):
        sll[-1]

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

def test_memory_management():
    import gc
    gc.collect()
    dll = DoublyLinkedList()
    for i in range(1000):
        dll.append(i)
    assert len(dll) == 1000
    del dll
    gc.collect()
    assert gc.garbage == []

def test_performance_get_set():
    sll = SinglyLinkedList()
    for i in range(1000):
        sll.append(i)
    assert sll[999] == 999
    with pytest.raises(IndexError):
        sll[1000]
    with pytest.raises(IndexError):
        sll[-1]

def test_singly_linked_list_negative_index():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(IndexError):
        sll[-2]

def test_doubly_linked_list_insert_out_of_bounds():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(IndexError):
        dll.insert(2, 2)

def test_singly_linked_list_set_out_of_bounds():
    sll = SinglyLinkedList()
    sll.append(1)
    with pytest.raises(IndexError):
        sll[1] = 2