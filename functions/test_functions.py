import pandas as pd
import random

group_names = ["Group A","Group B","Group C","Group D","Group E","Group F","Group G","Group H","Group I","Group J","Group K","Group L"]

df = pd.read_csv('test.csv')

# test group draw
def group_draw(g, n):

    # getting number of groups from group_names list
    groups = group_names[:g]

    # selecting number of pots by amount of teams per group
    for i in range(n):

        # collecting list of teams in the pot
        pot = df.loc[g * i: (i + 1) * g - 1]["Country"].tolist()
        # shuffling the pot
        random.shuffle(pot)

        # drawing number of groups
        for j in range(g):

            # if drawing first team it creates list
            if i == 0:
                groups[j] = [pot[j]]

            # otherwise, it appends new team to the list
            else:
                groups[j].append(pot[j])

    # printing the groups
    for i in range(g):
        print(f"{group_names[i]}: {', '.join(groups[i])}")

group_draw(10, 12)