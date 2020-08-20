def additives(N: int, dct_mprod: dict) -> list:
    """
    Decompose an integer into its component additives
    """
    if N == 1:
        return {'maxproduct': 1, 'components': [1]}

    components = []
    maxprod = float('-inf')
    for i in range(1, N//2 + 1):
        balance = N - i

        if balance not in dct_mprod.keys():
            dct_mprod[balance] = additives(balance, dct_mprod)

        thisprod = i * balance
        thiscomponent = [balance]
        if i * dct_mprod[balance]['maxproduct'] > thisprod:
            thisprod = i * dct_mprod[balance]['maxproduct']
            thiscomponent = dct_mprod[balance]['components']

        if thisprod > maxprod:
            maxprod = thisprod
            components = [i] + thiscomponent

    return {'maxproduct': maxprod, 'components': components}


def maxproduct(N: int) -> list:
    return additives(N, {})['maxproduct']


if __name__ == '__main__':
    print(maxproduct(10))