"""Prints whether each number in the input is odd or even."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Oddities

from sys import stdin, stdout

for line in stdin:
    num = int(line)
    parity = ""
    if num % 2:
        parity = "odd"
    else:
        parity = "even"
    stdout.write(f'{num} is {parity}\n')
