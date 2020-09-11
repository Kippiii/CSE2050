"""Prints fizz, buzz, or fizzbuzz depending on divisibility of numbers."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Fizz Buzz

from sys import stdin, stdout

x, y, n = map(int, stdin.readline().split())

for i in range(1, n+1):
    fizz = i % x == 0
    buzz = i % y == 0
    if fizz and buzz:
        stdout.write("FizzBuzz\n")
    elif fizz:
        stdout.write("Fizz\n")
    elif buzz:
        stdout.write("Buzz\n")
    else:
        stdout.write(f'{i}\n')
