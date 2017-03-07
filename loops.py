#!/usr/bin/python
"""Guess the number game"""

import random

value = random.randint(1, 10)
num = 0

while num != value:
    num = int(raw_input('Which number am I thinking of? '))

    if num != value:
        print 'Incorrect! Try again!'

print 'Finally!'
