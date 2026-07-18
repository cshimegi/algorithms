"""
Given an arrary of integers to represent the memory staet,
and a list of queries, each query is a pair of integers (allocation_type, number of allocations)
or (erase_type, ID), where ID is the number issued when the memory was allocated successfully.
When memory is allocated, it always allocates the smallest possible memory block that is not already allocated.
Each memory block has 8 bits, so memory allocation must start with index 0, 8, 16, 24, etc.
When memory can be allocated, all values in the memory state array are flipped to 1.
When memory can be erased, all values in the memory state array are flipped to 0.
When memory cannot be allocated or erased, the memory state array remains unchanged.

memory_state = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
queries = [
    (0, 3),
    (0, 2),
    (0, 4),
    (1, 4),
    (0, 1),
    (1, 2),
], where 0 is allocation type and 1 is erase type.

If allocation is successful, record the first index of the memory block that is allocated.
If erase is successful, record the length of the memory block that is erased.
otherwise, record -1 for each query.

output = [8, -1, -1, -1, -1, -1]
"""


def solve(memory_state: list[int], queries: list[tuple[int, int]]) -> list[int]:
    memory = memory_state[:]
    allocations: dict[int, int] = {}  # start_index -> length
    results = []

    for query_type, value in queries:
        if query_type == 0:
            results.append(_allocate(memory, value, allocations))
        elif query_type == 1:
            results.append(_erase(memory, value, allocations))
        else:
            results.append(-1)

    return results


def _allocate(memory: list[int], n: int, allocations: dict[int, int]) -> int:
    for pos in range(0, len(memory) - n + 1, 8):
        if not any(memory[pos : pos + n]):
            memory[pos : pos + n] = [1] * n
            allocations[pos] = n
            return pos
    return -1


def _erase(memory: list[int], block_id: int, allocations: dict[int, int]) -> int:
    if block_id not in allocations:
        return -1
    n = allocations.pop(block_id)
    memory[block_id : block_id + n] = [0] * n
    return n


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_given_example():
    memory = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    queries = [(0, 3), (0, 2), (0, 4), (1, 4), (0, 1), (1, 2)]
    assert solve(memory, queries) == [8, -1, -1, -1, -1, -1]


def test_alloc_from_block_zero():
    # All zeros: first allocation should land at index 0
    memory = [0] * 16
    assert solve(memory, [(0, 4)]) == [0]


def test_alloc_skips_to_next_aligned_block():
    # Block 0 (0-7) partially occupied; block 1 (8-15) free
    memory = [1] + [0] * 15
    assert solve(memory, [(0, 1)]) == [8]


def test_alloc_exactly_fills_block():
    memory = [0] * 16
    result = solve(memory, [(0, 8), (0, 8)])
    assert result == [0, 8]


def test_alloc_larger_than_memory_fails():
    memory = [0] * 8
    assert solve(memory, [(0, 9)]) == [-1]


def test_alloc_exact_memory_size():
    memory = [0] * 8
    assert solve(memory, [(0, 8)]) == [0]


def test_erase_then_reallocate():
    memory = [0] * 16
    queries = [
        (0, 8),  # allocate 8 bits at 0  → id=0
        (1, 0),  # erase id=0            → length=8
        (0, 8),  # re-allocate 8 bits    → should land at 0 again
    ]
    assert solve(memory, queries) == [0, 8, 0]


def test_erase_nonexistent_id_returns_minus_one():
    memory = [0] * 16
    assert solve(memory, [(1, 99)]) == [-1]


def test_erase_wrong_id_leaves_memory_unchanged():
    memory = [0] * 16
    queries = [
        (0, 4),   # allocates at 0
        (1, 99),  # wrong id → -1, memory must not change
        (0, 4),   # bits 4-7 still 1, block 0 not free; check block 8
    ]
    result = solve(memory, queries)
    assert result == [0, -1, 8]


def test_erase_returns_correct_length():
    memory = [0] * 24
    queries = [
        (0, 5),  # → id=0, length=5
        (1, 0),  # → 5
    ]
    assert solve(memory, queries) == [0, 5]


def test_alloc_does_not_mutate_input():
    memory = [0] * 16
    original = memory[:]
    solve(memory, [(0, 4)])
    assert memory == original


def test_multiple_allocations_fill_blocks_in_order():
    memory = [0] * 32
    queries = [(0, 2), (0, 3), (0, 1)]
    # Block 0: alloc 2 bits at 0, then alloc 3 bits must start at next aligned = 8
    # Block 1: alloc 1 bit at 8? No — bits 8-10 are already taken by previous alloc.
    # bits 8,9,10 taken → bit 11 still 0, but next aligned start is 16.
    result = solve(memory, queries)
    assert result == [0, 8, 16]


def test_full_memory_no_space():
    memory = [1] * 16
    assert solve(memory, [(0, 1)]) == [-1]


def test_partial_block_prevents_large_alloc():
    # One bit set in block 0 prevents 2-bit alloc there; block 1 is free
    memory = [0] * 16
    memory[0] = 1
    assert solve(memory, [(0, 2)]) == [8]


def test_erase_id_zero():
    # ID=0 is valid (first aligned position)
    memory = [0] * 16
    queries = [(0, 3), (1, 0)]
    assert solve(memory, queries) == [0, 3]


def test_sequential_alloc_erase_alloc():
    memory = [0] * 16
    queries = [
        (0, 8),  # id=0
        (0, 8),  # id=8
        (1, 0),  # erase id=0 → 8
        (0, 4),  # block 0 now free → 0
        (0, 4),  # bits 4-7 still 1 in block 0, block 1 full → -1 ...
                 # wait: block 0 has bits 0-3 = 1 (just allocated), bits 4-7 = 0
                 # but block 0 starts at 0, need 4 consecutive 0s starting at aligned pos
                 # pos=0: bits 0-3 = [1,1,1,1] ✗; pos=8: bits 8-15 = [1,...] ✗ → -1
    ]
    assert solve(memory, queries) == [0, 8, 8, 0, -1]


if __name__ == "__main__":
    tests = [
        test_given_example,
        test_alloc_from_block_zero,
        test_alloc_skips_to_next_aligned_block,
        test_alloc_exactly_fills_block,
        test_alloc_larger_than_memory_fails,
        test_alloc_exact_memory_size,
        test_erase_then_reallocate,
        test_erase_nonexistent_id_returns_minus_one,
        test_erase_wrong_id_leaves_memory_unchanged,
        test_erase_returns_correct_length,
        test_alloc_does_not_mutate_input,
        test_multiple_allocations_fill_blocks_in_order,
        test_full_memory_no_space,
        test_partial_block_prevents_large_alloc,
        test_erase_id_zero,
        test_sequential_alloc_erase_alloc,
    ]

    passed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}")

    print(f"\n{passed}/{len(tests)} passed")
