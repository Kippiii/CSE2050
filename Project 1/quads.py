"""Prints the quadrant where a specific point sits in the coordinate plane."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Quads Workout

from sys import stdin, stdout

x = int(stdin.readline())
y = int(stdin.readline())

solution = ""
if x > 0 and y > 0:
    solution = "I"
elif x < 0 and y > 0:
    solution = "II"
elif x < 0 and y < 0:
    solution = "III"
else:
    solution = "IV"

stdout.write(f'{solution}\n')
