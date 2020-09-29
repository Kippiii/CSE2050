"""Sort a group of numbers in Sharkovsky order."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Sharkovsky Ordering

from sys import stdin, stdout


def LSB(num):
    """Compute least significant bit of a number."""
    return num & -num


for line in stdin:
    nums = [int(i) for i in line.split()]
    # Sorts based on tuple as follows:
    #   1. Whether number is power of two
    #   2. Highest power of two multiple (inverted if number is power of two)
    #   3. Odd part of number other than multiple of two
    nums.sort(key=lambda num: (num == LSB(num),
                               LSB(num) if num != LSB(num) else -LSB(num),
                               num // LSB(num)), reverse=True)
    stdout.write(" ".join([str(num) for num in nums]))
    stdout.write("\n")
