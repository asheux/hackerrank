#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queens_attack(n, k, r_q, c_q, obstacles):
    """
    n: an integer, the number of rows and columns in the board 
    k: an integer, the number of obstacles on the board 
    r_q: integer, the row number of the queen's position 
    c_q: integer, the column number of the queen's position
    - obstacles: a two dimensional array of integers where each
    element is an array of integers, the row and column of an obstacle
    """
    dir_coords = {
            "n": (0, 1),
            "e": (1, 0),
            "w": (-1, 0),
            "ne": (1, 1),
            "nw": (-1, 1),
            "s": (0, -1),
            "se": (1, -1),
            "sw": (-1, -1),
            }
    directions = ["n", "e", "w", "ne", "nw", "s", "sw", "se"]
    count = 0

    obstacles_dict = {}
    for vector in obstacles:
        obstacles_dict[(vector[0] - 1) * n + vector[1]] = "No way"

    for d in directions:
        q_v = r_q, c_q
        for i in range(n):
            coord = list(sum(x) for x in zip(dir_coords[d], q_v))
            key = (coord[0] - 1) * n + coord[1]
            if key not in obstacles_dict:
                q_v = coord
                if (0 < coord[0] <= n) and (0 < coord[1] <= n):
                    count += 1
    return count


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queens_attack(n, k, r_q, c_q, obstacles)

    print(result)
