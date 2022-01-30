import random
import pandas as pd
# from functions.testing_zone_B import add_score_1, add_score_2

teams = ["England", "Italy", "Spain", "France", "Brazil"]

def group_simulation(teams):

    # only works currently if N even

    # for odd
    if len(teams) % 2 != 0:

        teams.append("dummy")

    n = len(teams)


    # number_of_matches can be replaced by either group_size - 1 or 2 * (group_size - 1) depending on number of legs
    for j in range(n - 1):

        print(f"\nRound {j + 1}")

        for i in range(int(n / 2)):

            if i == 0:

                participants = teams[0:2]
                random.shuffle(participants)
                if 'dummy' in participants:
                    pass
                else:
                    print(participants)
                # run match function(teams, ...)

            else:

                home, away = teams[i + 1], teams[n - i]
                participants = [home, away]
                random.shuffle(participants)
                if 'dummy' in participants:
                    pass
                else:
                    print(participants)
                # run match function(teams, ...)

        teams.insert(1, teams.pop())

group_simulation(teams)
