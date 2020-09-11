"""Takes two values for lattitude and longitude, makes the values discrete."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Discretizing the Sphere

from sys import stdin, stdout
from math import ceil, fmod, floor

n, m = map(int, stdin.readline().split())

for line in stdin:
    phi, lamb = map(float, line.split())
    # Converts phi to the range [0, 180) so that it maps to the grid
    phi = fmod(phi + 90, 180)
    if phi < 0:
        phi += 180
    phi = 180 - phi
    # Converts lambda to the range [0, 360) so that it maps to the grid
    lamb = fmod(lamb + 180, 360)
    if lamb < 0:
        lamb += 360
    # Maps phi and lambda x and y
    x = ceil(phi / (180 / (2*n))) - 1
    y = floor(lamb / (360 / (2*m)))
    stdout.write(f'{x}, {y}\n')
