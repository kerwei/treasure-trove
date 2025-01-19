def count_array(n: int, k: int, x:int) -> int:
    i = root = leaf = 1
    child = 0

    while i < n -1:
        child = leaf - child
        root = leaf - root
        leaf = pow(k -1, i)

        i += 1

    terminal = root if x == 1 else child

    return (k-1) * child + root - terminal


def count_array_modulo(n: int, k: int, x: int) -> int:
    return count_array(n, k, x) % (pow(10, 9) + 7)


if __name__ == '__main__':
    """
    Your goal is to find the number of ways to construct an array such that 
    consecutive positions contain different values. Specifically, we want to 
    construct an array with n elements such that each element between 1 and k, 
    inclusive. We also want the first and last elements of the array to be 1 and x.
    Given n, k and x, find the number of ways to construct such an array. 
    Since the answer may be large, only find it modulo 10**9 + 7.
    """

    # 266262299
    print(count_array_modulo(33260, 96055, 24745))