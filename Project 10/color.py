"""Prints UN entry order grouped together by country"""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Tri-Color Sort

from sys import stdin, stdout

# Creates a list for each country
australia = []
canada = []
us = []

# Compares last three digits of ids to figure out country
for line in stdin:
    line = line.strip()
    index = int(line[-3:])
    if index == 36:
        australia.append(line)
    elif index == 124:
        canada.append(line)
    elif index == 840:
        us.append(line)

# Prints all of the ids in proper order
for id in australia:
    stdout.write(f'{id}\n')
for id in canada:
    stdout.write(f'{id}\n')
for id in us:
    stdout.write(f'{id}\n')
