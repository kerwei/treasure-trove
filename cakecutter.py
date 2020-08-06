"""
Given a set of cakes with different radii to be shared amongst n people, find
the largest slice that can be cut and served to each person. Each slice should
be a full cut and not a combination of 2 smaller slices.
"""

import math

SIG = 9

def area(r: int) -> float:
    return math.pi * r * r

def nslices(A: list, size: float) -> float:
    slices = 0
    for a in A:
        slices += int(area(a) // size)

    return slices

def solution(n: int, A: list) -> list:
    if n == 1:
        return area(max(A))

    lower = size = 0
    upper = area(max(A))

    # Find the largest slice using binary search
    while round(lower, SIG) < round(upper, SIG):
        mid = (lower + upper)/2
        print(mid)

        if nslices(A, mid) >= n:
            lower = mid
            size = mid
        else:
            upper = mid

    return size


if __name__ == '__main__':
    A = [1.5, 2, 5, 3]

    size = solution(3, A)
    print([int(area(a)//size) for a in A])