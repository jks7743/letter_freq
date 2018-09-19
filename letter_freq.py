"""
Simple letter frequency script used for analyzing shift and swap ciphers
"""

__author__ = "Joshua Schenk"

import string

LETTER_DICT = dict.fromkeys(string.ascii_lowercase, 0)
LETTER_COUNT = 0

with open("input.txt", 'r') as file:
    for line in file:
        for ch in line:
            for letter in LETTER_DICT:
                if letter == ch:
                    LETTER_DICT[letter] += 1
                    LETTER_COUNT += 1

for letter in LETTER_DICT:
    print(letter + " " + str((LETTER_DICT[letter] / LETTER_COUNT) * 100))
