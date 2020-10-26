from typing import List


def rotate(d: int, arr: List):
    l = len(arr)
    d = d % l

    first = arr[d:]
    last = arr[:d]

    result = [*first, *last]
    print(result, first, last, d, l)

a = [1, 2,3,4,5]
rotate(4, a)
