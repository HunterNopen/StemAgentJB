# queue1

## Signature
Primary API is class-based:
- `Queue.enqueue(item) -> None`
- `Queue.dequeue() -> Any`
- `Queue.peek() -> Any | None`
- `Queue.clear() -> None`
- `len(Queue)` via `__len__`

## Contract
Implements a linked-list FIFO queue.

- `enqueue` adds item to back.
- `dequeue` removes and returns front item.
- `peek` returns front item without removing it.
- `clear` resets queue to empty state.

## Rules
- Internal pointers: `front`, `back`, and `size`.
- Empty dequeue raises `ValueError`.
- Empty peek returns `None`.
- `size` increments on enqueue and decrements on dequeue.

## Edge cases
- Dequeue on empty queue -> raises `ValueError`
- Peek on empty queue -> `None`
- Sequence enqueue/dequeue preserves FIFO order
- After `clear`, length is `0` and both pointers are `None`
