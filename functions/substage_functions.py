import pandas as pd
import random


def group_draw(group_number, group_size):

    # these are currently for testing purposes
    group_names = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F", "Group G", "Group H", "Group I",
                   "Group J", "Group K", "Group L"]
    df = pd.read_csv('test.csv')

    # getting number of groups from group_names list
    groups = group_names[:group_number]

    # selecting number of pots by amount of teams per group
    for i in range(group_size):

        # collecting list of teams in the pot
        pot = df.loc[group_number * i: (i + 1) * group_number - 1]["Country"].tolist()
        # shuffling the pot
        random.shuffle(pot)

        # drawing number of groups
        for j in range(group_number):

            # if drawing first team it creates list
            if i == 0:
                groups[j] = [pot[j]]

            # otherwise, it appends new team to the list
            else:
                groups[j].append(pot[j])

    # printing the groups
    for i in range(group_number):
        print(f"{group_names[i]}: {', '.join(groups[i])}")

    return groups


# def wc_group_draw():

    # TODO: draw teams with correct rules for confederation numbers
    
# def wc_group_draw_slow():

    # TODO: draw one team at a time to add suspense to the draw

def group_simulation(teams, legs):

    # TODO: create group dataframe

    # # for odd numbered groups we append a dummy team for correct fixture order
    if len(teams) % 2 != 0:

        teams.append("dummy")

    n = len(teams)

    # number of matchdays to simulate is legs multiplied number of teams minus one
    for j in range(legs * (n - 1)):

        # proof of function working
        print(f"\nRound {j + 1}")

        # number of matches is number of teams / 2
        for i in range(int(n / 2)):

            # fixture scheduling works by having element 0 v element 1 first
            if i == 0:

                participants = teams[0:2]
                # printing as proof of function
                if 'dummy' in participants:
                    pass
                else:
                    print(participants)
                # TODO: add run match function(teams, ...)

            # then the remaining teams play from out to in
            else:

                home, away = teams[i + 1], teams[n - i]
                participants = [home, away]
                # printin as proof of function
                if 'dummy' in participants:
                    pass
                else:
                    print(participants)
                # TODO: add run match function(teams, ...)

        # second element of list moved to back, functions like 2 column system for drawing fixtures where all teams
        # except a fixed team cycle clockwise
        teams.insert(1, teams.pop())

    # return final group table

# Variable Glossary
# group_names - list of group names, also used as variable generate groups variable from
# groups - list containing all groups which are themselves lists stored within the list 'groups'
# pot - contains group_number teams, seeded group that teams are distributed into the groups from, one team per pot goes into each group
# group_number - number of groups
# group_size - number of teams in each group
