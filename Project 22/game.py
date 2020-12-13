# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Save The Manatee (Game)
"""Control manatee to get as many points as possible."""

import argparse
import urllib.request
import pygame
import io

# Saves information regarding the various image files
link_begin = "http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050"
link_begin += "/projects/save/icons/"
links = {
    "M": "hugh.png",
    "W": "injured.png",
    "#": "coquina.png",
    "*": "boat.png",
    "\\": "hyacinth.png",
    "G": "grate.png",
    "O": "open.png",
    ".": "seagrass.png",
    " ": "water.png"
}

# Loads the images from the URLs
images = {}
for key in links.keys():
    file = io.BytesIO(urllib.request.urlopen(link_begin + links[key]).read())
    images[key] = pygame.image.load(file)

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
        map.append([s for s in tmp.decode().rstrip()])

# Saves the size of the grid
grid_length = len(map)
grid_width = 0

# Saves the location of important entities in the map
manatee_pos = []
grate_pos = []
hyacinth_pos = []
for i in range(len(map)):
    for j in range(len(map[i])):
        grid_width = max(grid_width, len(map[i]))
        if map[i][j] == "M":
            manatee_pos = [i, j]
        elif map[i][j] == "G":
            grate_pos = [i, j]
        elif map[i][j] == "\\":
            hyacinth_pos.append([i, j])

for i in range(len(map)):
    if len(map[i]) < grid_width:
        map[i] += [" " for _ in range(grid_width - len(map[i]))]

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
        map[new_pos[0]][new_pos[1]] = "M"
        map[manatee_pos[0]][manatee_pos[1]] = " "
        manatee_pos = new_pos
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
                        map[new_boat_pos[0] + 1][new_boat_pos[1]] = "W"
    return "injured" if hit_manatee else None


# Handles case of no hyacinths
if len(hyacinth_pos) == 0:
    map[grate_pos[0]][grate_pos[1]] = "O"

# Calculates the size of the window for the game
max_length = 800
max_width = 800
tile_size = 0
if grid_length >= grid_width:
    tile_size = max_length // grid_length
else:
    tile_size = max_width // grid_width
length = tile_size * grid_length
width = tile_size * grid_width

# Scales the images to the proper size
for key in images.keys():
    images[key] = pygame.transform.scale(images[key], (tile_size, tile_size))

# Initializes the instance of Pygame
pygame.init()
display = pygame.display.set_mode((width, length))
pygame.display.set_caption("Save the Manatee!")
clock = pygame.time.Clock()
crashed = False

# Initializes the font
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 50, bold=True)

score = 0
end_reason = None
while not crashed:  # Loops until game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN and end_reason is None:
            # Makes move based on pressed key
            if event.key == pygame.K_LEFT or event.key == pygame.K_l:
                move = (0, -1)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_r:
                move = (0, 1)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_d:
                move = (1, 0)
            elif event.key == pygame.K_UP or event.key == pygame.K_u:
                move = (-1, 0)
            elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                move = (0, 0)
            elif event.key == pygame.K_a:
                score = hyacinths * 50 - moves
                end_reason = "quit"
                break
            else:
                continue

            # Makes the move and update map
            end_reason = make_move(move)
            if end_reason is None:
                end_reason = move_boats()
            moves += 1

    # Adds in the images within the grid
    display.fill((255, 255, 255))
    start_x = 0
    start_y = 0
    for line in map:
        for c in line:
            display.blit(images[c], (start_x, start_y))
            start_x += tile_size
        start_x = 0
        start_y += tile_size

    # Adds the text to the screen
    if end_reason is not None:
        if end_reason == 'win':
            color = (0, 255, 0)
            score = hyacinths*75 - moves
        elif end_reason == 'injured':
            color = (255, 0, 0)
            score = hyacinths*25 - moves
        else:
            color = (0, 0, 0)
            score = hyacinths*50 - moves
        text = font.render(f'{end_reason}', False, color)
        display.blit(text, (width - 150, 20))
    else:
        score = hyacinths*25 - moves

    # Adds score information to screen
    text = font.render(f"Score: {score}", False, (0, 0, 0))
    display.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
