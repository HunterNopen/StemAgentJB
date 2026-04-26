# binarySearchTree1

## Signature
Primary API is class-based:
- `BinaryTree()`
- `BinaryTree.add(value) -> None`
- `BinaryTree.remove(val) -> None`
- `BinaryTree.getMin() -> Any`
- `BinaryTree.getMax() -> Any`
- `target in BinaryTree` via `__contains__`
- `BinaryTree.closest(target) -> Any | None`
- `iter(BinaryTree)` in-order traversal

## Contract
Implements a non-balanced binary search tree with duplicates inserted to the left subtree.

- Tree starts empty.
- `add` inserts values while preserving BST ordering rule used by this implementation.
- `remove` deletes one matching value if present.
- `getMin`/`getMax` raise `ValueError` on empty tree.
- `closest` returns nearest value to target, or `None` if tree is empty.

## Rules
- Insertion:
  - `val <= node.value` goes left
  - `val > node.value` goes right
- Removal:
  - If node has no left child, replacement is right child.
  - Otherwise predecessor from left subtree (right-most node of left subtree) is promoted.
- Iteration yields in-order traversal of stored values.
- Membership check uses iterative BST walk.

## Edge cases
- Empty tree: `getMin` / `getMax` -> raises `ValueError`
- Empty tree: `closest(target)` -> `None`
- Removing missing value leaves tree unchanged
- Duplicate inserts are permitted and placed in left subtree
- Membership on empty tree returns `False`
