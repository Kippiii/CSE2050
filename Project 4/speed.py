"""Calculates distance travelled based on speed and time given by users."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Speed Limit

from sys import stdin, stdout

while True:
    n = int(stdin.readline())
    if n == -1:
        break

    distance = 0
    prev_time = 0
    for _ in range(n):
        speed, time = map(int, stdin.readline().split())
        distance += speed * (time - prev_time)
        prev_time = time

    stdout.write(f'{distance} miles\n')
