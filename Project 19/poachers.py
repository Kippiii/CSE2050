# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Poachers!
"""Calculate the safety of manatees based on their positions."""

from sys import stdin, stdout
from scipy.spatial import ConvexHull, qhull


def is_in_hull(hull, point):
    """Determine whether point is within convex hull."""
    if hull is None:
        return False

    for i in range(len(hull.vertices)):
        j = i + 1 if i != len(hull.vertices) - 1 else 0
        a = hull.points[hull.vertices[i]]
        b = hull.points[hull.vertices[j]]
        dot_product = ((a[1] - b[1]) * (point[0] - a[0])) \
            + ((b[0] - a[0]) * (point[1] - a[1]))
        if dot_product < 0:
            return False
    return True


# Accepts input for the program
w, p, m = map(int, stdin.readline().split())
wardens = [list(map(int, stdin.readline().split())) for _ in range(w)]
poachers = [list(map(int, stdin.readline().split())) for _ in range(p)]
manatees = [list(map(int, stdin.readline().split())) for _ in range(m)]

# Generates the two convex hulls needed for the program
try:
    warden_hull = ConvexHull(wardens)
except qhull.QhullError:
    warden_hull = None
try:
    poacher_hull = ConvexHull(poachers)
except qhull.QhullError:
    poacher_hull = None

# Loops through each manatee that was input
for m in manatees:
    safe = is_in_hull(warden_hull, m)
    endangered = is_in_hull(poacher_hull, m)

    # Prints the status of each manatee
    status = ""
    if safe:
        status = "safe"
    elif endangered:
        status = "endangered"
    else:
        status = "vulnerable"
    stdout.write(f'Manatee at ({m[0]}, {m[1]}) is {status}.\n')
