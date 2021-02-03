import itertools

from typing import List


def password(A: List, N: int) -> List:
    """
    Return all possible combination of passwords of a specified length from
    list. Where two or more element words are combined, they are concatenated
    by an underscore. For example, 
    given A = ['one', 'A', 'list', 'of', 'random', 'words'], 
    password(A, 5) should return ['one_A', 'A_one', 'words', 'A_A_A', 'of_of']
    """
    # Allocate list members into buckets of length
    dct = {i:[] for i in range(1, max([len(a) for a in A]) + 1)}
    for a in A:
        dct[len(a)] += [a]

    combo = [None] * (N + 1)

    if dct.get(1):
        combo[1] = [tuple([1])]
    
    if dct.get(2):
        combo[2] = [tuple([2])]

    # Apply dynamic programming to discover the possible configurations to
    # achieve the desired pass word length. Use list position indexing
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

    # For all configurations that are applicable to a given password length,
    # generate all password outputs through a product operation between all
    # members
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