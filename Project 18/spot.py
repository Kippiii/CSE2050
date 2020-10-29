"""Compute whether a dice can end up in a certain state."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Spot On
from sys import stdin, stdout
from string import digits
from collections import namedtuple

# Accepting input from the system
n = int(stdin.readline())
grid = [list(stdin.readline().strip()) for _ in range(n)]

# Finding the start and goal within the grid
Point = namedtuple("Point", ["x", "y"])
for x in range(n):
    for y in range(n):
        if grid[x][y] == "M":
            start = Point(x, y)
        elif grid[x][y] in digits:
            goal = Point(x, y)

# Saves whether a node has been visitted
in_state = [[[[False for _ in range(6)] for _ in range(6)]
            for _ in range(n)] for _ in range(n)]

stack = []
stack.append((start.x, start.y, 6, 3, 4, 5, 2))

# Runs Depth-First Search
while stack:
    (x, y, bottom, up, down, left, right) = stack.pop()
    if x < 0 or x >= n or y < 0 or y >= n:
        continue
    if grid[x][y] == "*" or in_state[x][y][bottom-1][up-1]:
        continue
    in_state[x][y][bottom-1][up-1] = True
    # For going up
    stack.append((x - 1, y, up, 7 - bottom, bottom, left, right))
    # For going down
    stack.append((x + 1, y, down, bottom, 7 - bottom, left, right))
    # For going left
    stack.append((x, y - 1, left, up, down, 7 - bottom, bottom))
    # For going right
    stack.append((x, y + 1, right, up, down, bottom, 7 - bottom))

# Prints the answer
if True in in_state[goal.x][goal.y][int(grid[goal.x][goal.y])-1]:
    stdout.write("Yes\n")
else:
    stdout.write("No\n")
