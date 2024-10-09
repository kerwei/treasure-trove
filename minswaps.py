from typing import List, Mapping, Optional


def minswaps_new(arr: List[int]) -> int:
    """
    You are given an unordered array consisting of consecutive positive integers 
    [1, 2, 3, ..., n] without any duplicates.
    You are allowed to swap any two elements.
    Find the minimum number of swaps required to sort the array in ascending order.
    """
    # Init the array indexer
    arr_idx: List[int] = [-1] * (max(arr) + 1)
    # Index the array by value
    for i, a in enumerate(arr):
        arr_idx[a] = i

    # count of swap
    nswap: int = 0
    # working variables
    _original_idx: int = 0
    _displaced_value: Optional[int] = None

    # arr_idx is sorted; we'll check for non -1 values
    for j, v in enumerate(arr_idx):
        if v < 0:
            continue

        # Found value. If already in the correct location, continue
        if v == _original_idx:
            _original_idx += 1
            continue

        # Swap is required. Back up the value to be replaced
        _displaced_value = arr[_original_idx]
        # Slot the correct value into the required index
        arr[_original_idx] = j              # This may not be necessary since we process from left to right
        # Put the displaced value into the space previously occupied by the invader
        arr[v] = _displaced_value
        # Also update the new address of the displaced value
        arr_idx[_displaced_value] = v

        _original_idx += 1
        nswap += 1

    return nswap


if __name__ == '__main__':
    print(minswaps_new([6, 4, 1, 2, 3, 5]))