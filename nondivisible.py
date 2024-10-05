from typing import List, Mapping, Set


def non_divisible_subset(k: int, s: List[int]) -> int:
    """
    Given a set of distinct integers, return the size of a maximal subset of S
    where the sum of any 2 numbers in S is not evenly divisible by k.
    """
    if len(s) == 1:
        return 1 if s[0] % k != 0 else 0
    elif len(s) == 2:
        return 2 if sum(s) % k != 0 else 0

    s_int: Set = set(s)
    distinct_int: List[int] = sorted(s_int)
    minsum: int = distinct_int[0] + distinct_int[1]
    maxsum: int = distinct_int[-1] + distinct_int[-2]

    k_multiple: List[int] = [x for x in range(minsum, maxsum) if x % k == 0]

    dict_factors: Mapping[int, List[int]] = {x: [] for x in distinct_int}

    # Get a tally of all factors
    for x in k_multiple:
        bal: int = distinct_int[-1]

        for curr in distinct_int:
            if curr >= bal or curr >= x:
                break

            bal = x - curr
            if bal == curr or not s_int.intersection(set([bal])):
                continue

            dict_factors[curr].append(bal)
            dict_factors[bal].append(curr)

    nondivisors = distinct_int
    # Drop factors from list
    factors = sorted([x for x in dict_factors.items() if x[1]],
        key=lambda y: y[1], reverse=True)
    
    for f in factors:
        if not dict_factors[f[0]]:
            continue

        nondivisors.remove(f[0])
        for v in f[1]:
            dict_factors[v].remove(f[0])

        dict_factors[f[0]] = []

    return len(nondivisors)


if __name__ == '__main__':
    print(non_divisible_subset(4, [19, 10, 12, 10, 24, 25, 11]))