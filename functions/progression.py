import math

def progression(groups, straight, intermediate):

    x = math.floor(straight / len(groups))

    # qualified_a have gone straight through (straight)
    qualified_a = []

    for i in range(len(groups)):
        idx = groups[i].index.to_list()
        qualified_a.extend(idx[0:x])

    # TO DO: As