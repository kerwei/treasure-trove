def distinct_slice(M, A):
    if len(A) == 1:
        return 1
    # write your code in Python 3.6
    M += 1
    dupe = [-1] * M
    idxhead = idxtail = 0
    nunique = 0

    while idxhead < len(A) - 1:
        while idxtail < len(A):
            if dupe[A[idxtail]] < 0:
                dupe[A[idxtail]] = idxtail
            else:
                idxdupe = dupe[A[idxtail]]
                nunique += (((idxtail - idxhead) * (idxtail - idxhead + 1)) / 2) - (((idxtail - idxdupe - 1) * (idxtail - idxdupe)) / 2)

                for i in range(idxhead, idxdupe + 1):
                    dupe[A[i]] = -1

                dupe[A[idxtail]] = idxtail
                idxhead = idxdupe + 1

            idxtail += 1

        idxtail -= 1
        nunique += ((idxtail - idxhead + 1) * (idxtail - idxhead + 2)) / 2
        idxhead = idxtail

    return int(nunique)


if __name__ == '__main__':
    A = [3, 4, 5, 5, 2]
    # A = [1, 2]
    # A = [2, 4, 4, 5, 5, 6]
    print(distinct_slice(6, A))