"""Calculates the number of stitches in a knitting project."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Knitting

from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
pattern = [int(i) for i in stdin.readline().split()]

# Creating an array containing the sum of pattern values
sum_pattern = [0]
prev_val = 0
for i in range(k):
    sum_pattern.append(pattern[i] + sum_pattern[i] + prev_val)
    prev_val += pattern[i]
excess = prev_val  # Stores the excess stitches in each run of the pattern

full_patterns = (m - 1) // k
# Uses equation sum(i) = n(n - 1) / 2 for changing input into pattern
overlap = (full_patterns * (full_patterns - 1)) // 2 * excess
# Computes number of stitches from repeating pattern
stitches = n * m + overlap * k + sum_pattern[-1] * full_patterns

excess_rows = (m - 1) % k
# Adds in extra stitches for partial pattern
stitches += full_patterns * excess * excess_rows + sum_pattern[excess_rows]

stdout.write(f'{stitches}\n')
