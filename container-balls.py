#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    """
    nc: represents next container
    c: represents the current container
    t: represents the type of balls in the container
    nt: represents the next type in the container
    """
    m1 = container
    result = ""

#     for c in range(len(m1)):
#         nc = (c + 1) % len(m1)
    counts = {c: 0 for c in range(len(m1))}

    for cx in range(len(m1)):
        for tx in range(len(m1[cx])):
            counts[cx] += m1[tx][cx]

    for c in range(len(m1)):
        t = c
        nc = (c + 1) % len(m1[c])
        nt = nc

        if m1[nc][t] > 0 < m1[c][nt]:
            if m1[nc][t] < m1[c][nt]:
                m1[c][nt] -= m1[nc][t]
                m1[c][t] += m1[nc][t]
                m1[nc][nt] += m1[nc][t]
                m1[nc][t] = 0
            elif m1[nc][t] > m1[c][nt]:
                m1[nc][t] -= m1[c][nt]
                m1[c][t] += m1[c][nt]
                m1[nc][nt] += m1[c][nt]
                m1[c][nt] = 0
            else:
                temp = m1[c][nt]
                m1[c][t] += temp
                m1[nc][nt] += temp
                m1[c][nt], m1[nc][t] = 0, 0

    for i, v in enumerate(m1):
        s = sum(v)
        if s == counts[i]:
            result = "Possible"
        else:
            result = "Impossible"
    print(result)


if __name__ == '__main__':

    q = int(input('Enter number of queries: '))

    for q_itr in range(q):
        n = int(input('Enter number of rows and column: '))

        container = []

        for i in range(n):
            container.append(list(map(int, input(f'Enter {n} row {i} values sep by space: ').rstrip().split())))

        result = organizingContainers(container)

        print(result)
