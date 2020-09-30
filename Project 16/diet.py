"""Calculate an even split between amount of food eaten in two days."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Pickerel Weed

from sys import stdin, stdout

weights = [int(line) for line in stdin]

weights.sort(reverse=True)
midpoint = sum(weights) // 2  # Saves the max value of the solution
first_day = []  # Stores the values to be printed
cur_sum = 0  # Stores the current sum of values

# Greedily takes largest bunch that keeps it within range
for w in weights:
    if cur_sum + w <= midpoint:
        cur_sum += w
        first_day.append(w)

stdout.write(" ".join(str(i) for i in first_day[::-1]))
stdout.write("\n")
