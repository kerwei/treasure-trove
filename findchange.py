from typing import List


def find_change(amt: int, k: List[int]) -> int:
    """ For a given set of denominations, you are asked to find the minimum number of coins with
        which a given amount of money can be paid. Assume that you can use as many coins of
        a particular denomination as necessary.
    """
    prev_tally: List[int] = [float('inf')] * (amt + 1)

    for c in range(len(k)):
        coin = k[c]
        c_tally: List[int] = [0] * (amt + 1)

        for i in range(1, amt + 1):
            if i < coin:
                c_tally[i] = prev_tally[i]
                continue
            elif i == coin:
                c_tally[i] = 1
            else:
                c_tally[i] = min(
                    c_tally[i % coin] + (i//coin) * c_tally[coin], prev_tally[i])

        prev_tally = c_tally

    return prev_tally


if __name__ == '__main__':
    print(find_change(6, [1, 3, 4]))