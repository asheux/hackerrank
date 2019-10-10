"""
imports
"""
from functools import reduce


# Complete the extraLongFactorials function below.
def extra_long_factorials(number):
    """
    computes factorial of an integer (n)
    n: an integer
    """
    if 1 <= number <= 100:
        result = reduce(lambda x, y: x * y, list(range(1, number + 1)))
        print(result)


if __name__ == '__main__':
    N = int(input())

    extra_long_factorials(N)
