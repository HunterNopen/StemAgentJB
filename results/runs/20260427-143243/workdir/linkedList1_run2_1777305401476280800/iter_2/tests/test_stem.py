from source import SinglyLinkedList, DoublyLinkedList, SinglyLinkedNode, DoublyLinkedNode
import pytest

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
    a = object()
    b = object()
    sll.append(a)
    sll.append(b)
    assert a in sll
    assert b in sll
    assert object() not in sll

def test_singly_linked_list_next():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.cursor = sll.head
    assert sll.next() == 1
    assert sll.next() == 2
    with pytest.raises(StopIteration):
        sll.next()

def test_doubly_linked_list_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert len(dll) == 3
    assert dll[0] == 1
    assert dll[1] == 2
    assert dll[2] == 3

def test_doubly_linked_list_cursor_management():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.cursor = dll.head
    assert dll.next() == 1
    assert dll.next() == 2
    assert dll.next() == 3
    with pytest.raises(StopIteration):
        dll.next()
    dll.cursor = dll.head.next
    assert dll.previous() == 1
    with pytest.raises(StopIteration):
        dll.previous()

def test_doubly_linked_list_contains():
    dll = DoublyLinkedList()
    a = object()
    b = object()
    dll.append(a)
    dll.append(b)
    assert a in dll
    assert b in dll
    assert object() not in dll

def test_doubly_linked_list_get_set():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll[1] = 5
    assert dll[1] == 5
    with pytest.raises(IndexError):
        dll[3]
    with pytest.raises(IndexError):
        dll[-1]

def test_singly_linked_list_negative_index():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(IndexError):
        sll[-2]

def test_doubly_linked_list_previous():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.cursor = dll.head.next
    assert dll.previous() == 1
    with pytest.raises(StopIteration):
        dll.previous()

def test_singly_linked_list_empty_next():
    sll = SinglyLinkedList()
    with pytest.raises(StopIteration):
        sll.next()

def test_singly_linked_list_contains_identity():
    sll = SinglyLinkedList()
    a = []
    b = []
    sll.append(a)
    assert a in sll
    assert b not in sll

def test_doubly_linked_list_contains_identity():
    dll = DoublyLinkedList()
    a = []
    b = []
    dll.append(a)
    assert a in dll
    assert b not in dll

def test_singly_linked_list_set_out_of_bounds():
    sll = SinglyLinkedList()
    sll.append(1)
    with pytest.raises(IndexError):
        sll[1] = 2

def test_doubly_linked_list_set_out_of_bounds():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(IndexError):
        dll[1] = 2

def test_singly_linked_list_append_none():
    sll = SinglyLinkedList()
    sll.append(None)
    assert sll[0] is None

def test_doubly_linked_list_append_none():
    dll = DoublyLinkedList()
    dll.append(None)
    assert dll[0] is None

def test_singly_linked_list_length():
    sll = SinglyLinkedList()
    assert len(sll) == 0
    sll.append(1)
    assert len(sll) == 1
    sll.append(2)
    assert len(sll) == 2
    sll.append(3)
    assert len(sll) == 3

def test_doubly_linked_list_length():
    dll = DoublyLinkedList()
    assert len(dll) == 0
    dll.append(1)
    assert len(dll) == 1
    dll.append(2)
    assert len(dll) == 2
    dll.append(3)
    assert len(dll) == 3

def test_singly_linked_list_get_set_out_of_bounds():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(IndexError):
        sll[2] = 3

def test_doubly_linked_list_insert_out_of_bounds():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(IndexError):
        dll.insert(2, 2)