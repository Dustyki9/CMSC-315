"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import random
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    In the worst case (the target is the last element, or is
    not in the list at all), every single element must be
    visited exactly once. Because the number of comparisons
    grows in direct proportion to the number of items (n) in
    the list, the running time scales linearly with the size
    of the input -- hence O(n). There is no way to "skip"
    elements because the list is not assumed to be sorted or
    indexable in any special way.
    """
    for index in range(len(lst)):       # visit every position, in order
        if lst[index] == target:        # compare current element to target
            return index                # found it -- stop early (best case)
    return -1                           # reached the end without a match
    


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

      Each comparison eliminates half of the remaining search
    space. Starting with n elements, after 1 comparison there
    are n/2 left, after 2 comparisons n/4, after k comparisons
    n/2^k. The search ends when only one element remains, i.e.
    when n/2^k = 1, which means k = log2(n). So the number of
    comparisons needed grows logarithmically with n, making
    binary search dramatically faster than linear search on
    large, sorted datasets.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid                  # found the target
        elif lst[mid] < target:
            # Target must be in the right half (if it exists at all),
            # since the list is sorted and everything at/left of mid
            # is too small. Shrink the window from the left.
            low = mid + 1
        else:
            # Target must be in the left half. Shrink the window
            # from the right.
            high = mid - 1
 
    return -1                           # low > high means window is empty

def time_search(search_func, lst, target):
    """Helper: run a search function and report index + elapsed time."""
    start = time.perf_counter()
    result = search_func(lst, target)
    elapsed = time.perf_counter() - start
    return result, elapsed
    

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # both algorithms return the correct index.
    small_data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
 
    print("\n=== SMALL DATASET TEST ===")
    print(f"Dataset: {small_data}")
 
    existing_value = 45     # present at index 7
    missing_value = 99      # not present at all
 
    for target in (existing_value, missing_value):
        lin_result, lin_time = time_search(linear_search, small_data, target)
        bin_result, bin_time = time_search(binary_search, small_data, target)
        print(f"\nSearching for {target}:")
        print(f"  Linear search -> index {lin_result}  ({lin_time:.8f}s)")
        print(f"  Binary search -> index {bin_result}  ({bin_time:.8f}s)")
    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.
    # efficiency gap between O(n) and O(log n) clearly measurable.
    
    large_size = 1_000_000
    large_data = list(range(0, large_size * 2, 2))  # sorted even numbers
 
    print("\n=== LARGE DATASET TEST ===")
    print(f"Dataset size: {large_size:,} sorted elements")
 
    existing_value = large_data[-1]     # last element: worst case for linear search
    missing_value = large_data[-1] + 1  # an odd number that can't be in the list
 
    for label, target in (("EXISTING (last element)", existing_value),
                           ("MISSING", missing_value)):
        lin_result, lin_time = time_search(linear_search, large_data, target)
        bin_result, bin_time = time_search(binary_search, large_data, target)
        print(f"\nSearching for {label} value ({target}):")
        print(f"  Linear search -> index {lin_result}  ({lin_time:.6f}s)")
        print(f"  Binary search -> index {bin_result}  ({bin_time:.6f}s)")
        if lin_time > 0 and bin_time > 0:
            print(f"  Binary search was ~{lin_time / bin_time:,.0f}x faster")
 
    # Explanation:
    # Linear search must scan close to a million elements to find
    # the last value (or to determine a value is missing), so its
    # time grows directly with dataset size (O(n)).
    # Binary search only needs about log2(1,000,000) ≈ 20 comparisons
    # to do the same job (O(log n)). As the dataset grows, this gap
    # widens dramatically -- doubling the data barely changes binary
    # search's time but doubles linear search's time.
 
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
     # Edge case 1: Empty list.
    # Neither function has any elements to inspect, so both should
    # immediately return -1 without error.
    empty_list = []
    print("\n1) Empty list:")
    print(f"   linear_search([], 5) -> {linear_search(empty_list, 5)} "
          f"(expected -1: no elements to check)")
    print(f"   binary_search([], 5) -> {binary_search(empty_list, 5)} "
          f"(expected -1: low=0 > high=-1, loop never runs)")
 
    # Edge case 2: Single-element list.
    # Tests the smallest non-trivial case for both a hit and a miss.
    single = [7]
    print("\n2) Single-element list [7]:")
    print(f"   linear_search([7], 7) -> {linear_search(single, 7)} "
          f"(expected 0: only element matches)")
    print(f"   binary_search([7], 7) -> {binary_search(single, 7)} "
          f"(expected 0: mid = 0 immediately matches)")
    print(f"   linear_search([7], 3) -> {linear_search(single, 3)} "
          f"(expected -1: no match found)")
    print(f"   binary_search([7], 3) -> {binary_search(single, 3)} "
          f"(expected -1: window shrinks to empty immediately)")
 
    # Edge case 3: Target at the very first position.
    # Best case for linear search (1 comparison); binary search
    # takes its normal log(n) path but still finds it correctly.
    data = [1, 3, 5, 7, 9, 11, 13]
    print(f"\n3) Target at first position, list {data}, target=1:")
    print(f"   linear_search -> {linear_search(data, 1)} "
          f"(best case for linear: found on first comparison)")
    print(f"   binary_search -> {binary_search(data, 1)} "
          f"(binary search still narrows down to index 0 correctly)")
 
    # Edge case 4: Target at the very last position.
    # Worst case for linear search (must scan the whole list);
    # binary search remains efficient regardless of position.
    print(f"\n4) Target at last position, list {data}, target=13:")
    print(f"   linear_search -> {linear_search(data, 13)} "
          f"(worst case for linear: must check every element)")
    print(f"   binary_search -> {binary_search(data, 13)} "
          f"(binary search finds it in just a couple of comparisons)")
 
 


if __name__ == "__main__":
    main()
