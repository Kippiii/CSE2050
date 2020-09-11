"""Takes two values for lattitude and longitude, makes the values discrete."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Discretizing the Sphere

from sys import stdin, stdout
from math import ceil, fmod
from decimal import Decimal

n, m = map(int, stdin.readline().split())

for line in stdin:
    phi, lamb = map(Decimal, line.split())
    # Converts phi to the range [0, 180] so that it maps to the grid
    phi = fmod(phi + 90, 180)
    if phi < 0:
        phi += 180
    phi = 180 - phi
    # Converts lambda to the range [0, 360] so that it maps to the grid
    lamb = fmod(lamb + 180, 360)
    if lamb < 0:
        lamb += 360
    # Maps phi and lambda x and y
    x = ceil(phi / (180 / (2*n))) - 1
    y = ceil(lamb / (360 / (2*m))) - 1
    if y < 0:
        y = 0  # Deals with 180 degree edge case
    stdout.write(f'{x}, {y}\n')
