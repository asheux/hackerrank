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

    for c in range(len(m1)):
        nc = (c + 1) % len(m1)
        t = c
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
        print(c, nc, m1[c])

        # sub[c] = {i: value for i, value in enumerate(m1[c])}

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

