"""Solve the Flood puzzle using a greedy algorithm."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Flood

from sys import stdin, stdout

# Saves all possible movement directions
DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def flood(x, y, grid, visited, counter):
    """Use floodfill to see which color to set on each move."""
    if visited[x][y]:
        return

    visited[x][y] = True
    if grid[x][y] != grid[0][0]:
        # Counts grid spaces that are not original color
        counter[grid[x][y]] += 1

    for dir in DIRECTIONS:
        if 0 <= x + dir[0] < len(grid) and 0 <= y + dir[1] < len(grid[0]):
            # Always continues if on flooded color
            if grid[x][y] == grid[0][0]:
                flood(x + dir[0], y + dir[1], grid, visited, counter)
            else:
                # Continues if staying on same color if other than original
                if grid[x][y] == grid[x + dir[0]][y + dir[1]]:
                    flood(x + dir[0], y + dir[1], grid, visited, counter)


grid = []
for line in stdin:
    grid.append([int(i) for i in line.strip()])

# Saves the solution of the problem
times_colors = [0 for i in range(7)]
while True:
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    # Counts the number of each color that would be changed
    counter = [0 for i in range(7)]
    flood(0, 0, grid, visited, counter)

    max_ind = 0  # Saves the color that will need to be changed to
    for i in range(1, len(counter)):
        if counter[i] > counter[max_ind]:
            max_ind = i
    if counter[max_ind] == 0:
        break  # Ends loop if every tile is same color
    times_colors[max_ind] += 1

    # Updates the colors of for the next stage of the program
    changed_color = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j] and grid[i][j] == changed_color:
                grid[i][j] = max_ind

stdout.write(f'{sum(times_colors)}\n')
stdout.write(" ".join([str(times_colors[i]) for i in range(1, 7)]))
stdout.write("\n")
