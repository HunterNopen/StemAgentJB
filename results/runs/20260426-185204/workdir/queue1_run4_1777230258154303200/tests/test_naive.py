import pytest
from source import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    assert len(q) == 1
    assert q.peek() == 1
    q.enqueue(2)
    assert len(q) == 2
    assert q.peek() == 1
    q.enqueue(3)
    assert len(q) == 3
    assert q.peek() == 1

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert len(q) == 2
    assert q.peek() == 2
    assert q.dequeue() == 2
    assert len(q) == 1
    assert q.peek() == 3
    assert q.dequeue() == 3
    assert len(q) == 0

def test_dequeue_empty():
    q = Queue()
    with pytest.raises(ValueError):
        q.dequeue()

def test_peek():
    q = Queue()
    assert q.peek() is None
    q.enqueue(1)
    assert q.peek() == 1
    q.dequeue()
    assert q.peek() is None

def test_clear():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert len(q) == 3
    q.clear()
    assert len(q) == 0
    assert q.peek() is None

def test_fifo_order():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

def test_multiple_clears():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.clear()
    assert len(q) == 0
    q.clear()
    assert len(q) == 0

def test_enqueue_none():
    q = Queue()
    q.enqueue(None)
    assert len(q) == 1
    assert q.peek() is None
    assert q.dequeue() is None
    assert len(q) == 0

def test_enqueue_dequeue_mixed():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    with pytest.raises(ValueError):
        q.dequeue()