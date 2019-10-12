#!/bin/python3
"""
imports
"""


# Complete the climbingLeaderboard function below.
def climbing_leaderboard(scores, alice):
    """
    Takes in an array of integers that represent leaderboard scores
    and an array of integers that represent Alice's scores
    then returns an integer array where each element res[j]
    represents Alice's rank after the jth game.
    """

    myrank = 1
    ranks = []

    for index, element in enumerate(scores):
        currentelem = element
        nextelem = scores[(index + 1) % len(scores)]
        rank = myrank

        if currentelem == nextelem:
            ranks.append(rank)
        else:
            myrank += 1
            ranks.append(rank)
    return get_alice_ranks(scores, ranks, alice)


def get_alice_ranks(scores, ranks, alice_score):
    """
    compute rank for alice
    """
    al_ranks = []
    for _, score in enumerate(alice_score):
        first_score = scores[0]
        last_score = scores[-1]
        if score > first_score:
            al_ranks.append(ranks[0])
        elif score < last_score:
            al_ranks.append(ranks[-1] + 1)
        else:
            rank = binary_search(scores, score)
            al_ranks.append(ranks[rank])
    return al_ranks


def binary_search(scores, score):
    """
    binary search algo
    """
    # mid = (low + high)// 2
    first = 0
    last = len(scores) - 1

    while first <= last:
        mid = (first + last) // 2

        if scores[mid] == score:
            return mid
        elif scores[mid] < score < scores[mid - 1]:
            return mid
        elif scores[mid] > score >= scores[mid + 1]:
            return mid + 1
        elif scores[mid] > score:
            first = mid + 1
        elif scores[mid] < score:
            last = mid - 1


if __name__ == '__main__':
    SCORES_COUNT = int(input("Enter number of players: "))
    GAME_SCORES = list(map(
        int,
        input("Enter the leaderboard scores(in desc): ").rstrip().split()))
    ALICE_COUNT = int(input("Enter the number games Alice plays: "))
    ALICE = list(map(
        int,
        input("Enter alice game scores: ").rstrip().split()))
    RESULT = climbing_leaderboard(GAME_SCORES, ALICE)

    print(RESULT)
