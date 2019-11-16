#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    S = s.replace(" ", "")
    L = len(S)
    floor = math.floor(L**0.5)
    ceil = math.ceil(L**0.5)
    grid = []
    result = ""
    if (floor * ceil) < L:
        fc = (floor, ceil)
        mn, mx = min(fc), max(fc)
        floor, ceil = mn + (mx - mn), mx

    for r in range(floor):
        ns = ""
        for c in range(ceil):
            if len(S) > c:
                ns += S[c]
        index = len(ns)
        S = S[index:]
        grid.append(ns)

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if len(grid[y]) > x:
                result += grid[y][x]
        result += " "
    return result

if __name__ == '__main__':
    s = input("Enter the string to encrypt: ")

    result = encryption(s)

    print(result)

