"""Estimate roots of complex polynomials."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Newton Basins

from sys import stdin, stdout


def deriv(roots, a):
    """Calculate derivative value based on product rule."""
    ans = 0
    for i in range(len(roots)):
        tmp = 1  # Equals one because being multiplied
        for j in range(len(roots)):
            if i != j:  # Uses fact that d/dx(x - r) = 1
                tmp *= a - roots[j]
        ans += tmp
    return ans


def value(roots, a):
    """Calculate the value of polynomial at point a."""
    ans = 1
    for root in roots:
        ans *= a - root
    return ans


roots = [complex(i) for i in stdin.readline().split()]

for line in stdin:
    x = complex(line)
    index = -1  # Sets -1 as default value
    for i in range(20):  # Goes through 20 tries
        val = value(roots, x)
        der = deriv(roots, x)
        if der == 0:  # Prevents division by zero
            break
        x -= val / der
        for j in range(len(roots)):  # Checks closeness of each root
            if abs(x - roots[j]) <= 10**(-5):
                index = j

    if index == -1:
        stdout.write('diverges\n')
    else:
        stdout.write(f'{index}\n')
