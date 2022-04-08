import pandas as pd
import random

from matchengine.multi_sim_engine import multi_sim_match

def group_draw(group_number, group_size, teams):
    # group number is an integer (number of groups)
    # group size is an integer (number of teams per group)
    # teams is a list

    # list of group names
    group_names = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F", "Group G", "Group H", "Group I",
                   "Group J", "Group K", "Group L"]

    # getting number of groups from group_names list
    groups = group_names[:group_number]

    # selecting number of pots by amount of teams per group
    for i in range(group_size):

        # collecting list of teams in the pot
        pot = teams[group_number * i: (i + 1) * group_number]
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


def group_simulation(data, teams, legs, sim, WC):
    # creating group table as pandas data frame and displaying empty group table
    group_table = pd.DataFrame(0, index=teams, columns=['P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])
    print(group_table)

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
                    if sim > 0:
                        data, score = multi_sim_match(data, participants, WC)
                    # if sim == 0:
                        # single_sim_match
                    group_table = match_update(group_table, participants, score)

            # then the remaining teams play from out to in
            else:

                home, away = teams[i + 1], teams[n - i]
                participants = [home, away]
                # printing as proof of function
                if 'dummy' in participants:
                    pass
                else:
                    if sim > 0:
                        data, score = multi_sim_match(data, participants, WC)
                    # if sim == 0:
                        # single_sim_match
                    group_table = match_update(group_table, participants, score)

        # second element of list moved to back, functions like 2 column system for drawing fixtures where all teams
        # except a fixed team cycle clockwise
        teams.insert(1, teams.pop())
        group_table = round_update(group_table)

    # return final group table
    print("\n", group_table)


def match_update(group_table, participants, score):

    # Result dependent updates
    if score[0] > score[1]:
        group_table.loc[participants[0], 'Pts'] = group_table.loc[participants[0], 'Pts'] + 3
        group_table.loc[participants[0], 'W'] = group_table.loc[participants[0], 'W'] + 1
        group_table.loc[participants[1], 'L'] = group_table.loc[participants[1], 'L'] + 1

    if score[0] < score[1]:
        group_table.loc[participants[1], 'Pts'] = group_table.loc[participants[1], 'Pts'] + 3
        group_table.loc[participants[1], 'W'] = group_table.loc[participants[1], 'W'] + 1
        group_table.loc[participants[0], 'L'] = group_table.loc[participants[0], 'L'] + 1

    if score[0] == score[1]:
        group_table.loc[participants, 'Pts'] = group_table.loc[participants, 'Pts'] + 1
        group_table.loc[participants, 'D'] = group_table.loc[participants, 'D'] + 1

    # Required updates (Home)
    group_table.loc[participants, 'P'] = group_table.loc[participants, 'P'] + 1
    group_table.loc[participants[0], 'GF'] = group_table.loc[participants[0], 'GF'] + score[0]
    group_table.loc[participants[0], 'GA'] = group_table.loc[participants[0], 'GA'] + score[1]
    group_table.loc[participants[1], 'GF'] = group_table.loc[participants[1], 'GF'] + score[1]
    group_table.loc[participants[1], 'GA'] = group_table.loc[participants[1], 'GA'] + score[0]

    return group_table

def round_update(group_table):

    group_table['GD'] = group_table['GF'] - group_table['GA']
    group_table = group_table.sort_values(['Pts', 'GD', 'GF', 'GA'], ascending=[False, False, False, True])

    return group_table

# Variable Glossary
# group_names - list of group names, also used as variable generate groups variable from
# groups - list containing all groups which are themselves lists stored within the list 'groups'
# pot - contains group_number teams, seeded group that teams are distributed into the groups from, one team per pot goes into each group
# group_number - number of groups
# group_size - number of teams in each group
