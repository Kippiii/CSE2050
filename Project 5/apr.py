"""Calculates payments made as well as the interest on the payments."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Annual Percentage Rate

from sys import stdin, stdout
from decimal import Decimal

balance, interest, payment = map(Decimal, stdin.readline().split())
# Allows decimal numbers to be integers
balance = round(balance * 100)
payment = round(payment * 100)
interest = interest / 100

# Prints the first line of output
stdout.write(f'{"payment":>7}{"balance":>14}{"interest":>14}\n')

payment_num = 0
net_interest = 0
# Loops through for each payment made
while True:
    stdout.write(f'{payment_num:>7}{balance//100:>11,}.{balance%100:>02}'
                 f'{net_interest//100:>11,}.{net_interest%100:>02}\n')
    if balance <= 0 or payment_num >= 100:
        break  # Ends program when balance is empty
    cur_interest = round(balance * interest / 12)
    balance -= payment
    net_interest += cur_interest
    balance += cur_interest
    payment_num += 1
    balance = max(0, balance)  # Prevents balance from being negative
