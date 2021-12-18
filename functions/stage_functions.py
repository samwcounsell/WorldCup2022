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

    # return groups

def wc_group_draw():

    # draw teams with correct rules for confederation numbers
    
def wc_group_draw_slow():

    # draw one team at a time to add suspense to the draw

# Variable Glossary
# group_names - list of group names, also used as variable generate groups variable from
# groups - list containing all groups which are themselves lists stored within the list 'groups'
# pot - contains group_number teams, seeded group that teams are distributed into the groups from, one team per pot goes into each group
# group_number - number of groups
# group_size - number of teams in each group