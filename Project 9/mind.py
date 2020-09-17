"""Calculates the scoring during one round of mastermind."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Master Mind

from sys import stdin, stdout
from string import ascii_uppercase

code, guess = stdin.readline().split()
duplicate = [False] * len(code)  # Saves whether a pair is a duplicate

# Computes the value for s
s = 0
for i in range(len(code)):
    if code[i] == guess[i]:
        duplicate[i] = True
        s += 1

# Computes the value for r
r = 0
code_freq = [0] * 26  # Saves the letter frequency of the code
guess_freq = [0] * 26  # Saves the letter frequency of the guess
for i in range(len(code)):
    if not duplicate[i]:  # Duplicate values are not counted for r
        code_freq[ascii_uppercase.find(code[i])] += 1
        guess_freq[ascii_uppercase.find(guess[i])] += 1
# Adds repeated letters to r
for i in range(26):
    r += min(code_freq[i], guess_freq[i])

stdout.write(f'{s} {r}\n')
