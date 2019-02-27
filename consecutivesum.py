import argparse
import time

N = 100
res = []
round2=lambda x, y=None: round(x+1e-15, y)

def startcount(n):
    """
    The conventional way of counting the number of subsets that sum up to n for
    a range of integers up to n. The cutoff is set to n/2 here as it is
    impossible for any numbers above n/2 to be able to sum up to exactly n.
    However, this does not make a difference in computation speed.
    """
    for i in range (1, int(n/2)):
        rsum = []
        while i < int(n/2):
            rsum.append(i)
            if sum(rsum) == n:
                res.append(rsum)
                break
            elif sum(rsum) > n:
                break
            i += 1


def whilecount(n):
    """
    For a given range n, determines the number of subsets of integers that sum
    up to exactly n.
    For subsets with even number of elements, each half of the subset is 
    symmetric. E.g. for a subset with 4 elements, element2 + element3 = 
    element1 + element4 = n /(0.5 x number of elements)
    For subsets with odd number of elements, each half of the subset is also 
    symmetric if the median is excluded. E.g. for a subset with 4 elements, 
    element2 + element4 = element1 + element4 = n - element3
    As each subset of specific length is unique i.e. it is not possible to find 
    more than 1 subset of consecutive integers of, say length 4, that sums up to
    20, this algorithm searches by traversing the possible lengths of a subset.
    The limit of the length is hit when the value of n/i is less than half the
    size of the subset. Since the range of numbers has a floor of zero, the 
    symmetric principle cannot be satisfied after that limit. This effectively
    sets the number of iteration to a maximum of root(2n)
    """
    # Consecutive numbers has a minimum length of 2
    i = 2
    # Numerical center of the subset
    avg = int(n/i)

    while avg >= round2(i/2):
        # Evens
        if i % 2 == 0:
            # E.g. (avg) + (avg + 1) * (2/2) = n
            if i * avg + i/2 == n:
                res.append([i for i in range(
                    (avg - int(i/2)) + 1, (avg + int(i/2) + 1))])
        else:
        # Odds
            # E.g. (avg - 1) + (avg + 1) + (avg) = n
            if i * avg == n:
                res.append([i for i in range(
                    (avg - int(i/2)), (avg + int(i/2) + 1))])

        i += 1
        avg = int(n/i)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        '-r', '--range', type=int, default=N,
        help="The range to decipher"
    )
    args = parser.parse_args()
    stime = time.perf_counter()
    # startcount(args.range)
    whilecount(args.range)
    elapsed = time.perf_counter() - stime
    print('Sets: %s\nElapsed: %s seconds' % (str(len(res)), str(elapsed)))