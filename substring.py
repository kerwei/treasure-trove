"""
Samantha and Sam are playing a numbers game. Given a number as a string, 
no leading zeros, determine the sum of all integer values of substrings of the 
string.

Given an integer as a string, sum all of its substrings cast as integers. 
As the number may become large, return the value modulo 10^9 + 7.

Example
n = '42'

Here n is a string that has 3 integer substrings: 4, 2 and 42. Their sum is 48, 
and 48 modulo (10^9 + 7) = 48.
"""
MOD = pow(10, 9) + 7


def substrings(n: str) -> int:
    globsum: int = 0
    prevsum: int = 0

    for i, r in enumerate(n):
        v = int(r)
        prevsum = (prevsum * 10) + (v * (i+1))

        globsum = (globsum + prevsum) % MOD

    return globsum


if __name__ == '__main__':
    # 445677619
    print(substrings('972698438521'))
