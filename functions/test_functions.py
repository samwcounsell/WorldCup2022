# Play area for testing and designing various functions

import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

    return groups

groups = group_draw(8, 4)

# Plot image in Python #

#img = mpimg.imread('test.jpg')
#imgplot = plt.imshow(img)
#plt.show()

# Testing displaying groups

x = 8

group_df = pd.DataFrame.from_records(groups)
group_df = group_df.T
group_df.columns = group_names[:x]

the_table = plt.table(cellText=group_df.values,
                      rowLoc='right',
                      colLabels=group_df.columns,
                      loc='center')
plt.axis('off')
plt.axis('tight')
the_table.auto_set_font_size(False)
the_table.set_fontsize(12)

# plt.show()