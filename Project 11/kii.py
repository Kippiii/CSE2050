"""Calculate the nth letter of the manatee speak string."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Manatee Vocalization

from sys import stdin, stdout


def find_kii(n, k=0, length=3):
    """Use recursion to determine nth letter."""
    if length < n:
        n = find_kii(n, k + 1, length * 2 + k + 4)
        if n <= 0:  # Returns when correct letter already found
            return -1
    prev_length = (length - k - 3) // 2
    n -= prev_length  # Removes leftmost k-1 sequence from n

    if n == 1:  # Leftmost value must be 'k'
        stdout.write("k\n")
        return -1
    elif n <= k + 3:  # Checks if one of k+2 'i's
        stdout.write("i\n")
        return -1
    n -= k + 3
    return n


n = int(stdin.readline())
find_kii(n)
