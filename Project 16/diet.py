"""Calculate an even split between amount of food eaten in two days."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Pickerel Weed

from sys import stdin, stdout

weights = [int(line) for line in stdin]

weights.sort(reverse=True)
midpoint = sum(weights) // 2  # Saves the max value of the solution

best_sum = 0  # Stores the highest sum that can be reached
best_sol = []  # Stores the best solution that can be found
# Greedily takes largest bunch that keeps it within range for each start
for i in range(len(weights)):
    cur_sum = 0  # Stores the current sum of values
    cur_sol = []  # Stores the current solution
    for j in range(i, len(weights)):
        w = weights[j]  # Stores the current weight
        if cur_sum + w <= midpoint:
            cur_sum += w
            cur_sol.append(w)
    if cur_sum > best_sum:  # Runs if new solution is better
        best_sum = cur_sum
        best_sol = cur_sol

for i in best_sol[::-1]:
    stdout.write(f'{i}\n')
