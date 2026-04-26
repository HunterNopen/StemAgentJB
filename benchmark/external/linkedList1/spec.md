# linkedList1

## Signature
Primary APIs:
- `SinglyLinkedList` with `append`, `__len__`, `__getitem__`, `__setitem__`, `__contains__`, iterator protocol (`__iter__`, `next`)
- `DoublyLinkedList` extending `SinglyLinkedList` with `append`, `insert`, `previous`

## Contract
Provides simple singly and doubly linked list structures with cursor-based iteration helpers.

- `append` adds element to tail.
- Index-based get/set is supported with O(n) traversal and raises `IndexError` for invalid index.
- `DoublyLinkedList.insert` inserts before selected index with pointer rewiring.

## Rules
- `__contains__` checks identity (`is`) rather than equality (`==`).
- `next()` advances internal cursor and raises `StopIteration` when cursor is `None`.
- `insert` in doubly list:
  - Raises `IndexError` for index >= size.
  - Handles head insertion, near-tail insertion path, and middle insertion.
- `size` is incremented on successful append/insert.

## Edge cases
- Access/set with negative or out-of-range index -> `IndexError`
- Membership depends on object identity semantics
- Calling `next()` past end -> `StopIteration`
- `previous()` when no previous node -> `StopIteration`
- Inserting into empty doubly list at index 0 initializes head/cursor
