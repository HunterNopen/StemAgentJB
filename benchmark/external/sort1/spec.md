# sort1

## Signature
Static methods on class `Sort`:
- `selection_sort(arr: list) -> list`
- `insertion_sort(arr: list) -> list`
- `merge_sort(arr: list) -> list`
- `merge(left: list, right: list) -> list`
- `quick_sort(arr: list, first: int, last: int) -> None`
- `partition(arr: list, first: int, last: int) -> int`

## Contract
Provides multiple sorting algorithms for orderable elements.

- Selection, insertion, and merge sort return list results.
- Quick sort sorts in-place over provided index range.

## Rules
- `selection_sort`: repeatedly selects minimum from unsorted suffix.
- `insertion_sort`: shifts larger prefix elements to insert current value.
- `merge_sort`: recursively splits list and merges sorted halves.
- `quick_sort`: recursive partitioning around last element pivot.
- `partition` returns final pivot index.

## Edge cases
- Empty list and single-element list remain unchanged
- Already sorted input remains sorted
- Duplicate values are retained
- `quick_sort` requires valid `first/last` bounds from caller
