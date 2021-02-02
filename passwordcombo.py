import itertools

from typing import List


def password(A: List, N: int) -> List:
    """
    Return all possible combinations of a password from list. Where two or
    more element words are combined, they are concatenated by an underscore
    """
    dct = {i:[] for i in range(1, max([len(a) for a in A]) + 1)}
    for a in A:
        dct[len(a)] += [a]

    combo = [None] * (N + 1)

    if dct.get(1):
        combo[1] = [tuple([1])]
    
    if dct.get(2):
        combo[2] = [tuple([2])]

    for i in range(3, N + 1):
        ctr = []
        for j in range(1, (i//2) + 1):
            ctr.append([tuple(
                itertools.chain(*ea)) for ea in itertools.product(
                    combo[i-j-1], combo[j])])

        if dct.get(i):
            combo[i] = list(itertools.chain(*ctr, [tuple([i])]))
        else:
            combo[i] = list(itertools.chain(*ctr))

    tracker = {}
    output = []
    for cmb in set(combo[-1]):
        sig = set([ea for ea in itertools.permutations(cmb)])

        for sg in sig:
            if tracker.get(sg):
                continue

            tracker[sg] = 1
            output += [
                '_'.join(x) for x in itertools.product(*[dct[s] for s in sg])]

    return output
