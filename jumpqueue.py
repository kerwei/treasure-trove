import math
from typing import List, Tuple, Union


def is_compliant(arr: List[int]) -> bool:
    """
    Returns True if the swapped queue does not breach a maximum limit of 2 swaps
    """
    goodq: List[int] = list(range(1, max(arr) + 1))
    return all(x - y <= 2 for x, y in zip(arr, goodq))


def mergesort(arr: List[int]) -> Tuple[int, List[int]]:
    """
    Sorts the given array into ascending order. Also count the number of swaps 
    (where a value is taken from the right, ahead of left) during the process 
    and return it as the first term of the output tuple
    """
    if not arr:
        return 0, []
    elif len(arr) == 1:
        return 0, arr
    elif len(arr) == 2:
        return (0, arr) if arr[0] <= arr[1] else (1, [arr[1], arr[0]])

    # Split array into 2 sides and use the mergesort on each, combining them afterwards
    mid = math.ceil(len(arr)//2)
    left = arr[:mid]
    right = arr[mid:]

    lswaps, left_sorted = mergesort(left)
    rswaps, right_sorted = mergesort(right)

    total_swaps = lswaps + rswaps
    sorted_queue: List[int] = []
    i = 0

    for k in range(len(left_sorted)):
        # Left is smaller than right
        if left_sorted[k] <= right_sorted[i]:
            sorted_queue.append(left_sorted[k])
            continue

        # Fill in from the right, as long as they are smaller than the current left value
        while i < len(right_sorted) and right_sorted[i] < left_sorted[k] :
            sorted_queue.append(right_sorted[i])
            # total_swaps needs to be increased by the number of position offset from the leftmost
            total_swaps += (len(left_sorted) - k)
            i += 1

        if i >= len(right_sorted):
            # Just fill up the sorted list with the remaining from the left
            sorted_queue.extend(left_sorted[k:])
            break

        sorted_queue.append(left_sorted[k])

    if i < len(right_sorted):
        sorted_queue.extend(right_sorted[i:])

    return total_swaps, sorted_queue


def jumpqueue(arr: List[int]) -> Union[str|int]:
    """
    Given an original array of consecutive positive integers forming a queue,
    1 being the head of the queue, and an input array arr where queue numbers
    have possibly been swapped, determine the number of queue swaps needed to 
    achieve the final queue arrangement. Each swap can only happen between 
    neighboring queue numbers and is also directional
    i.e. if 5 swapped with 4, it is considered a single jump even though 2 
    queue numbers switched places

    If a final queue positioning requires any number to swap more than twice,
    return 'Too chaotic'
    """
    if len(arr) < 2:
        return 0

    # Check if swap limit is breached
    if not is_compliant(arr):
        return 'Too chaotic'
    
    # Count the number of swaps to achieve the final queue order
    # --- use mergesort --- #
    swaps, _ = mergesort(arr)

    return swaps, _


if __name__ == '__main__':
    arr = [2, 1, 5, 3, 7, 8, 9, 6, 10, 4]
    print(jumpqueue(arr))
