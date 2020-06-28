import itertools
import math

from collections import defaultdict, Counter


def sieve(x: int) -> list:
    _out = [0] * (x + 1)
    _out[0] = _out[1] = 0
    i = 2

    while i <= math.sqrt(x):
        if not _out[i]:
            k = i ** 2
            while k <= x:
                # This condition ensures that only the smallest prime is
                # recorded. Necessary when coupled with the factorize function
                if not _out[k]:
                    _out[k] = i
                k += i

        i += 1

    return _out


class FactorsOfList:
    def __init__(self, x: list):
        self.x = x
        self.discovered = defaultdict(set)
        self.least_primes = sieve(max(x))

    def decompose(self, x, primes=None):
        if x in self.discovered:
            return self.discovered[x]

        leprime = self.least_primes[x]

        if leprime == 0:
            self.discovered[x] = self.discovered[x].union({x})
            return {x}

        self.discovered[x]= self.discovered[x].union({x})

        if not primes:
            primes = defaultdict(lambda: 0)

        primes[leprime] += 1
        self.discovered[x] = self.discovered[x].union(
            {leprime ** primes[leprime]})
        self.discovered[x] = self.discovered[x].union({i for i in itertools.chain(
            self.decompose(int(x/leprime), primes))})

        return self.discovered[x]

    def factorize(self):
        for x in self.x:
            yield self.decompose(x)


def solve(A: list):
    count_A = Counter(A)
    set_A = set(A)
    lnA = len(A)
    fktr = FactorsOfList(A)

    output = []
    for f in fktr.factorize():
        if f == {1}:
            output += [lnA - count_A[1]]
            continue

        output += [lnA - sum([count_A[d] for d in f]) - count_A[1]]

    return output


if __name__ == '__main__':
    A = [1, 2, 2, 2, 7, 14]
    fktr = FactorsOfList(A)
    print([f for f in fktr.factorize()])
    print(solve(A))