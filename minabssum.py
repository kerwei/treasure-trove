import random
import time


def components(A: list):
    """
    81% solution. Timeout for large inputs
    """
    A = sorted([abs(a) for a in A], reverse=True)
    totalA = sum(A)
    mid = (totalA + 1) // 2
    mindiff = float('inf')
    lsum = 0
    rsum = totalA

    i = j = 1
    A = [0] + A
    while i < len(A):
        rsum -= A[i-1]
        if rsum < mid:
            return min(mindiff, abs((2 * rsum) - totalA))

        lsum = 0
        j = i
        while j < len(A):
            lsum += A[j]

            if lsum == mid:
                return min(mindiff, abs(2 * lsum - totalA))

            if lsum > mid:
                lsum -= A[j]

            j += 1

        mindiff = min(mindiff, abs(2 * lsum - totalA))
        i += 1

    return min(mindiff, abs((2 * rsum) - totalA))


def slow_min_abs_sum(A):
    N = len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)

    S = sum(A)
    dp = [0] * (S+1)
    dp[0] = 1
    # print(str("j"), [1] + [s%10 for s in range(S)])

    for j in range(N):
        for i in range(S, -1, -1):
            if (dp[i] == 1) and (i + A[j] <= S):
                # print(f'r{j}', i, A[j])
                dp[i + A[j]] = 1

        # print(j, dp)

    result = S
    for i in range(S//2 + 1):
        if dp[i] == 1:
            result = min(result, S - 2 * i)

    return result


def golden_min_abs_sum(A):
    """
    Golden solution extracted from https://codility.com/media/train/solution-min-abs-sum.pdf
    """
    N = len(A)
    M = 0

    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)

    S = sum(A)
    count = [0] * (M + 1)

    for a in A:
        count[a] += 1

    dp = [-1] * (S + 1)
    dp[0] = 0
    print(0, [1]+[i for i in range(S+1)])
    # print('original dp:')
    # print(dp)

    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif j >= a and dp[j-a] > 0:
                    dp[j] = dp[j-a] - 1

    result = S
    for i in range(S//2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    
    return result


if __name__ == '__main__':
    # A = [1, 3, 4, 5, 7, 10]
    A = [1, 2, 5, 3, 4, 5, 2]
    # A = [40] * 20000
    # A[random.randint(0, 19999)] = 30

    start = time.time()
    print(golden_min_abs_sum(A))
    # print(components(A))
    print(f'{time.time() - start} s')