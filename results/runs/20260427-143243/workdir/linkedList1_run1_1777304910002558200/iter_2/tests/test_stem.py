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
    a = SinglyLinkedNode(1)
    b = SinglyLinkedNode(2)
    sll.append(a)
    sll.append(b)
    assert a in sll
    assert b in sll
    assert SinglyLinkedNode(3) not in sll

def test_doubly_linked_list_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert len(dll) == 3
    assert dll[0] == 1
    assert dll[1] == 2
    assert dll[2] == 3

def test_singly_linked_list_empty():
    sll = SinglyLinkedList()
    assert len(sll) == 0
    with pytest.raises(IndexError):
        sll[0]

def test_doubly_linked_list_empty():
    dll = DoublyLinkedList()
    assert len(dll) == 0
    with pytest.raises(IndexError):
        dll[0]

def test_doubly_linked_list_insert_head():
    dll = DoublyLinkedList()
    dll.append(2)
    dll.append(3)
    dll.insert(1, 0)
    assert dll[0] == 1
    assert dll[1] == 2
    assert dll[2] == 3

def test_doubly_linked_list_insert_out_of_bounds():
    dll = DoublyLinkedList()
    dll.append(1)
    with pytest.raises(IndexError):
        dll.insert(2, 2)

def test_doubly_linked_list_previous():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.cursor = dll.head.next
    assert dll.previous() == 1
    with pytest.raises(StopIteration):
        dll.previous()

def test_doubly_linked_list_cursor_management():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.next() == 1
    assert dll.next() == 2
    assert dll.next() == 3
    with pytest.raises(StopIteration):
        dll.next()

def test_singly_linked_list_negative_index():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(IndexError):
        sll[-1]

def test_doubly_linked_list_negative_index():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    with pytest.raises(IndexError):
        dll[-1]

def test_singly_linked_list_set_out_of_bounds():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    with pytest.raises(IndexError):
        sll[2] = 3