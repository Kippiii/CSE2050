"""Encrypts and decrypts strings using a Vigenère Cipher."""
# Author: Ian Orzel, iorzel2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Vigenère Cipher

from sys import stdin, stdout
from string import ascii_lowercase

key = stdin.readline().strip()
stdout.write(f'{key}\n')

for line in stdin:
    if line[0] == 'p':  # Runs when input is plaintext
        line = line[6:].strip()
        index = 0  # Index for key
        cipher = ""
        for c in line:
            if c in ascii_lowercase:
                new_letter_index = (ascii_lowercase.find(c)
                                    + ascii_lowercase.find(key[index])) % 26
                cipher += ascii_lowercase[new_letter_index]
                index = (index + 1) % len(key)
            else:
                cipher += c

        stdout.write(f'cipher {cipher}\n')
    elif line[0] == 'c':  # Runs when input is cipher text
        line = line[7:].strip()
        index = 0  # Index for key
        plain = ""
        for c in line:
            if c in ascii_lowercase:
                new_letter_index = (ascii_lowercase.find(c)
                                    - ascii_lowercase.find(key[index])) % 26
                plain += ascii_lowercase[new_letter_index]
                index = (index + 1) % len(key)
            else:
                plain += c

        stdout.write(f'plain {plain}\n')
