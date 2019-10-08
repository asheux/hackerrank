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
    al_ranks = []

    for _, a_score in enumerate(alice):
        al_scores = [*[a_score], *scores]
        ranks = get_ranks(al_scores)
        set_rank = {rank[0] for rank in ranks if rank[1] == a_score}
        al_ranks.append(*set_rank)
    return al_ranks


def get_ranks(scores):
    """
    compute rank for each player
    including alice
    """
    ranks = []
    sorted_scores = sorted(scores, reverse=True)
    myrank = 1

    for index, element in enumerate(sorted_scores):
        thiselem = element
        nextelem = sorted_scores[(index + 1) % len(sorted_scores)]
        (rank, score) = myrank, thiselem
        if thiselem == nextelem:
            ranks.append((rank, score))
        else:
            myrank += 1
            ranks.append((rank, score))
    return ranks


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
