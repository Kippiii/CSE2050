# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Save The Manatee (Game)
"""Control manatee to get as many points as possible."""

from sys import stdin, stdout
import argparse
import urllib.request

# Accepts the map URL input from the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--map', type=str)
args = parser.parse_args()

# Takes the map from URL
map = []
with urllib.request.urlopen(args.map) as f:
    while True:
        tmp = f.readline()
        if not tmp:
            break
        map.append([s for s in tmp.decode()[:-1]])

# Saves the location of important entities in the map
manatee_pos = []
grate_pos = []
hyacinth_pos = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "M":
            manatee_pos = [i, j]
        elif map[i][j] == "G":
            grate_pos = [i, j]
        elif map[i][j] == "\\":
            hyacinth_pos.append([i, j])

moves = 0
hyacinths = 0


def make_move(move):
    """Have manatee make move and update map."""
    global manatee_pos
    global hyacinths
    global hyacinth_pos

    # Ends the program if movement is out of bounds
    if move == (0, 0):
        return None
    new_pos = (manatee_pos[0] + move[0], manatee_pos[1] + move[1])
    if new_pos[0] < 0 or new_pos[0] >= len(map):
        return None
    if new_pos[1] < 0 or new_pos[1] >= len(map[new_pos[0]]):
        return None

    entity = map[new_pos[0]][new_pos[1]]
    if entity == "#" or entity == "G":
        # Runs if movement is impossible
        return None
    if entity == " " or entity == ".":
        # Runs if normal movement is possible
        map[new_pos[0]][new_pos[1]] = "M"
        map[manatee_pos[0]][manatee_pos[1]] = " "
        manatee_pos = new_pos
        return None
    if entity == "O":
        # Runs if manatee wins game
        return "win"
    if entity == "\\":
        # Runs if manatee eats hyacinth
        map[new_pos[0]][new_pos[1]] = "M"
        map[manatee_pos[0]][manatee_pos[1]] = " "
        manatee_pos = new_pos
        hyacinths += 1
        if len(hyacinth_pos) == hyacinths:
            map[grate_pos[0]][grate_pos[1]] = "O"
        return None
    if entity == "*":
        # Checks if manatee can push boat
        if move[0] == 0:
            new_boat_pos = (new_pos[0] + move[0], new_pos[1] + move[1])
            if new_boat_pos[0] < 0 or new_boat_pos[0] >= len(map):
                return None
            if new_boat_pos[1] < 0 \
                    or new_boat_pos[1] >= len(map[new_boat_pos[0]]):
                return None
            if map[new_boat_pos[0]][new_boat_pos[1]] == " ":
                map[new_boat_pos[0]][new_boat_pos[1]] = "*"
                map[new_pos[0]][new_pos[1]] = "M"
                map[manatee_pos[0]][manatee_pos[1]] = " "
                manatee_pos = new_pos
        return None
    return None


def move_boats():
    """Move boats downward properly."""
    hit_manatee = False
    for i in range(len(map)-1, -1, -1):
        for j in range(len(map[i])-1, -1, -1):
            if map[i][j] == "*":
                # Only runs if the entity is a boat
                if i + 1 >= len(map):
                    continue
                if map[i+1][j] == " ":
                    # Moves boat downward if possible
                    if i + 2 < len(map) and map[i+2][j] == "M":
                        hit_manatee = True
                        map[i+2][j] = "W"
                    map[i+1][j] = "*"
                    map[i][j] = " "
                elif map[i+1][j] == "*":
                    # Boats colliding with each other
                    new_boat_pos = (i, j)
                    if j + 1 < len(map[i]) and map[i][j+1] == " " \
                            and map[i+1][j+1] == " ":
                        new_boat_pos = (i+1, j+1)
                    elif j - 1 >= 0 and map[i][j-1] == " "  \
                            and map[i+1][j-1] == " ":
                        new_boat_pos = (i+1, j-1)
                    else:
                        continue

                    # Moves boat down to new position
                    map[i][j] = " "
                    map[new_boat_pos[0]][new_boat_pos[1]] = "*"
                    if new_boat_pos[0] + 1 < len(map) and \
                            map[new_boat_pos[0] + 1][new_boat_pos[1]] == "M":
                        hit_manatee = True
                        map[new_boat_pos[0] + 1][new_boat_pos[1]] == "W"
    return "injured" if hit_manatee else None


# Handles case of no hyacinths
if len(hyacinth_pos) == 0:
    map[grate_pos[0]][grate_pos[1]] = "O"

# Prints the beginning version of the map
for line in map:
    stdout.write(f'{"".join(line)}\n')
stdout.write('\n')

score = 0
end_reason = ""
while True:
    move_str = stdin.read(1)
    if move_str == "L":
        move = (0, -1)
    elif move_str == "R":
        move = (0, 1)
    elif move_str == "D":
        move = (1, 0)
    elif move_str == "U":
        move = (-1, 0)
    elif move_str == "W":
        move = (0, 0)
    elif move_str == "A":
        score = hyacinths * 50 - moves
        end_reason = "quit"
        break
    else:
        continue

    # Makes the move and update map
    result = make_move(move)
    if result is None:
        result = move_boats()

    # Print the current version of the map
    moves += 1
    for line in map:
        stdout.write(f'{"".join(line)}\n')
    stdout.write('\n')

    if result is not None:
        end_reason = result
        break

# Calculates the score of the player
if end_reason == "win":
    score = hyacinths * 75 - moves
elif end_reason == "injured":
    score = hyacinths * 25 - moves

stdout.write(f'{end_reason} {score}\n')
