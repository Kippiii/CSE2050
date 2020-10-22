"""Use Dijstra's to find the shortest paths starting from a node."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Shortest Path

import heapq
import gzip
import urllib.request
import argparse
from sys import stdout, stderr
from math import inf

# Dealing with the arguments of the program
parse = argparse.ArgumentParser()
parse.add_argument('--graph', type=str)
parse.add_argument('--source', type=int)
args = parse.parse_args()
args.graph = args.graph.strip()


def get_input(args):
    """Get the input from the given file."""
    # Tries to grab the contents of the file
    contents = ""
    try:
        # Unizips the file if it is local
        with gzip.open(args.graph, "rb") as f:
            contents = f.read()
    except Exception:
        try:
            # Downloads the file from url and unzips it
            contents = urllib.request.urlopen(args.graph).read()
            contents = gzip.decompress(contents)
        except Exception:
            stderr.write('This file does not exist!\n')
            return False

    contents = contents.decode("utf-8")
    contents = contents.splitlines()

    # Finds the first uncommented line
    index = 0
    while index < len(contents) and (len(contents[0]) == 0
                                     or contents[index][0] == "#"):
        index += 1
    # Ensures that the first line is formated properly
    try:
        n, e = map(int, contents[index].split())
    except Exception:
        return False
    if n < 0 or e < 0:
        return False

    # Generates the graph
    graph = [[] for _ in range(n+1)]
    edge_count = 0
    for i in range(index+1, len(contents)):
        # Skips commented lines
        if len(contents[i][0]) == 0 or contents[i][0] == "#":
            continue
        # Ensures that the graph file is formatted properly
        try:
            source, dest, weight = map(int, contents[i].split())
        except Exception:
            return False
        if source < 1 or source > n or dest < 1 or dest > n or weight < 0:
            return False

        graph[source].append((dest, weight))
        edge_count += 1

    # Ensures the correct number of edges
    if edge_count != e:
        return False

    return graph


graph = get_input(args)
if not graph or args.source < 1 or args.source >= len(graph):
    stderr.write("ERROR\n")
else:
    # Initializing dijkstra's
    q = []
    dist = [inf for _ in range(len(graph))]
    dist[0] = 0
    for i in range(1, len(graph)):
        heapq.heappush(q, (inf, i))
    dist[args.source] = 0
    heapq.heappush(q, (0, args.source))

    # Running dijkstra's
    while q:
        node = heapq.heappop(q)
        if node[0] < dist[node[1]]:
            continue
        for n in graph[node[1]]:
            new_dist = dist[node[1]] + n[1]
            if new_dist < dist[n[0]]:
                dist[n[0]] = new_dist
                heapq.heappush(q, (new_dist, n[0]))

    # Summing the distances together
    sum = 0
    for val in dist:
        if val is not inf:
            sum += val
    stdout.write(f'{sum}\n')
