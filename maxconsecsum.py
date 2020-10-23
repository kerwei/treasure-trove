def maxconsecsum(A):
    """
    For a given array of integers, begin from index 0, traverse to the end of
    the array, with the distance between 'steps' not larger than 6 indices.
    Find the maximum sum possible by traversing from one end to the other.
    """
    maxsum = A[0]
    nc = 0
    i = 1
    localmax = (0, float('-inf'))

    while i < len(A) - 1:
        if A[i] > 0:
            maxsum += A[i]
            nc = 0
            localmax = (0, float('-inf'))
        else:
            this_cell = maxsum + A[i]
            if this_cell >= localmax[1]:
                localmax = (i, this_cell)
                
            nc += 1
            if nc > 5:
                # At the maximum range, evaluate the best possible move
                # and commit the next step
                maxsum = localmax[1]
                nc = 0
                i = localmax[0]
                localmax = (0, float('-inf'))

        i += 1

    return maxsum + A[-1]