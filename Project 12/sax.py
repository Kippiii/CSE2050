"""Determine how many keys are pressed during sax performance."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Alto Saxophone

from sys import stdin, stdout

finger_guide = {  # Manually inputting saxaphone finger positions
    "c": [False, True, True, True, False, False, True, True, True, True],
    "d": [False, True, True, True, False, False, True, True, True, False],
    "e": [False, True, True, True, False, False, True, True, False, False],
    "f": [False, True, True, True, False, False, True, False, False, False],
    "g": [False, True, True, True, False, False, False, False, False, False],
    "a": [False, True, True, False, False, False, False, False, False, False],
    "b": [False, True, False, False, False, False, False, False, False, False],
    "C": [False, False, True, False, False, False, False, False, False, False],
    "D": [True, True, True, True, False, False, True, True, True, False],
    "E": [True, True, True, True, False, False, True, True, False, False],
    "F": [True, True, True, True, False, False, True, False, False, False],
    "G": [True, True, True, True, False, False, False, False, False, False],
    "A": [True, True, True, False, False, False, False, False, False, False],
    "B": [True, True, False, False, False, False, False, False, False, False]
}

for line in stdin:
    press_count = [0] * 10
    prev = [False] * 10  # It is first assumed that no keys are pressed
    for note in line.strip():
        for i in range(10):
            # Checks for key now being pressed
            if finger_guide[note][i] and not prev[i]:
                press_count[i] += 1
        prev = finger_guide[note]  # Updates prev to new key pattern
    for count in press_count:
        stdout.write(f'{count} ')
    stdout.write('\n')
