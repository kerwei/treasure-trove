from __future__ import annotations

from itertools import product
from typing import List, Tuple


def kSimilarity(s1: str, s2: str) -> int:
    """
    Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

    Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

    Constraints:

    1 <= s1.length <= 20
    s2.length == s1.length
    s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
    s2 is an anagram of s1.

    Example 3:

    Input: s1 = "abac", s2 = "baca"
    Output: 2

    """
    from string import ascii_lowercase

    mapper = {ch: [] for ch in ascii_lowercase[:6]}
    locs = []

    s1 = ''.join(s1.split())
    s2 = ''.join(s2.split())

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue

        mapper[s1[i]] += [i]
        locs += [i]

    class LinkedNode:
        def __init__(self, parent: LinkedNode, ch: str, idx: int):
            self.parent = parent
            self.ch = ch
            self.idx = idx

        def unset(self):
            mapper[self.ch].remove(self.idx)

            if self.parent:
                self.parent.unset()

    def test_swap(displace: List[LinkedNode]) -> None:
        """
        Breadth first search to find earliest termination
        """
        rs = []
        for node in displace:
            replace_with = s2[node.idx]
            for idy in mapper[replace_with]:
                if s2[idy] == node.ch:
                    mapper[replace_with].remove(idy)
                    node.unset()

                    return True, None
                else:
                    rs += [LinkedNode(node, replace_with, idy)]
        else:
            return False, rs

    gloswaps = 0
    for i in locs:
        nd = [LinkedNode(None, s1[i], i)]
        loswaps = 0
        rs = False

        while not rs:
            loswaps += 1
            rs, nd = test_swap(nd)

        gloswaps += loswaps

    return gloswaps


if __name__ == '__main__':
    s1 = "a b c c a a c c e e c d e e a"
    s2 = "b c a a c c e e c c d e a a e"

    print(kSimilarity(s1, s2))