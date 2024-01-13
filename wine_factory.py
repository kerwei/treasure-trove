"""
            F1. Wine Factory (Easy Version)
            time limit per test5 seconds
            memory limit per test512 megabytes
            inputstandard input
            outputstandard output

This is the easy version of the problem. The only difference between the two versions is the constraint on ci
and z. You can make hacks only if both versions of the problem are solved.

There are three arrays a, b and c. a and b have length n and c has length n−1 . Let W(a,b,c) denote the liters of wine created from the following process.

Create n water towers. The i-th water tower initially has ai liters of water and has a wizard with power bi in front of it. Furthermore, for each 1≤i≤n−1 , there is a valve connecting water tower i to i+1 with capacity ci.

For each i from 1 to n in this order, the following happens:

The wizard in front of water tower i removes at most bi liters of water from the tower and turns the removed water into wine.

If i≠n , at most ci liters of the remaining water left in water tower i flows through the valve into water tower i+1.

There are q
updates. In each update, you will be given integers p, x, y and z and you will update ap:=x, bp:=y and cp:=z. After each update, find the value of W(a,b,c). Note that previous updates to arrays a , b and c persist throughout future updates.

Input
The first line contains two integers n and q (2≤n≤5⋅105, 1≤q≤5⋅105) — the number of water towers and the number of updates.

The second line contains n integers a1,a2,…,an(0≤ai≤109) — the number of liters of water in water tower i.

The third line contains n integers b1,b2,…,bn (0≤bi≤109) — the power of the wizard in front of water tower i.

The fourth line contains n−1 integers c1,c2,…,cn−1 (ci=1018) — the capacity of the pipe connecting water tower i to i+1.

Each of the next q lines contains four integers p, x, y and z (1≤p≤n, 0≤x,y≤109, z=1018) — the updates done to arrays a, b and c.

Note that cn does not exist, so the value of z does not matter when p=n.

Output
Print q lines, each line containing a single integer representing W(a,b,c) after each update.
"""
import io
import os
import unittest
from unittest.mock import patch


def calc_total_wine_output():
    """ Accept inputs """
    lst_input = input().split(os.linesep)
    nbarrel, nupdate = (int(x) for x in lst_input[0].split())
    lst_barrel = [int(x) for x in lst_input[1].split()]
    lst_conversion = [int(x) for x in lst_input[2].split()]
    lst_tapsize = [int(x) for x in lst_input[3].split()] + [0]  # sentinel element

    nbarrel = int(nbarrel)
    nupdate = int(nupdate)
    arr_updates = [0] * nupdate
    for i in range(nupdate):
        arr_updates[i] = [int(x) for x in lst_input[4 + i].split()]

    # arr_updates.insert(0, [1, lst_barrel[0], lst_conversion[0], lst_tapsize[0]])

    for update in arr_updates:
        j, barrel, conversion, tapsize = update
        lst_barrel[j-1] = barrel
        lst_conversion[j-1] = conversion
        lst_tapsize[j-1] = tapsize

        output = 0
        carryover = 0
        cvolume = 0
        for i in range(nbarrel):
            cvolume = lst_barrel[i] + carryover
            coutput = lst_conversion[i] if cvolume > lst_conversion[i] else cvolume
            output += coutput
            carryover = max(cvolume - lst_conversion[i], 0)

        print(output)


class TestWineFactory(unittest.TestCase):
    @patch('builtins.input',
        side_effect=[os.linesep.join([
            '4 3',
            '3 3 3 3',
            '1 4 2 8',
            '1000000000000000000 1000000000000000000 1000000000000000000',
            '4 3 8 1000000000000000000',
            '2 5 1 1000000000000000000',
            '3 0 0 1000000000000000000'])])
    def test_three_updates(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            calc_total_wine_output()  # Call the function that takes input from stdin

            # Get the value that was printed to stdout
            printed_output = mock_stdout.getvalue().strip()

        # Perform your assertions on the printed output
        expected = os.linesep.join(['12', '12', '10'])
        self.assertEqual(printed_output, expected)

    @patch('builtins.input',
        side_effect=[os.linesep.join([
            '5 5',
            '10 3 8 9 2',
            '3 4 10 8 1',
            '1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000',
            '5 4 9 1000000000000000000',
            '1 1 1 1000000000000000000',
            '2 7 4 1000000000000000000',
            '4 1 1 1000000000000000000',
            '1 8 3 1000000000000000000'])])
    def test_five_updates(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            calc_total_wine_output()  # Call the function that takes input from stdin

            # Get the value that was printed to stdout
            printed_output = mock_stdout.getvalue().strip()

        # Perform your assertions on the printed output
        expected = os.linesep.join(['34', '25', '29', '21', '27'])
        self.assertEqual(printed_output, expected)