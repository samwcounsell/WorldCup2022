import math

import pandas as pd


def progression(groups, a, b):
    x = math.floor(a / len(groups))

    # qualified_a have gone straight through (straight)
    qualified_a, qualified_b = [], []

    for i in range(len(groups)):
        # Adding teams straight qualified to a list
        idx = groups[i].index.to_list()
        qualified_a.extend(idx[:x])

        # Removing qualified teams from groups to allow for extra teams to be calculated
        groups[i] = groups[i].iloc[x:]

    # TODO: Add system for if straight % groups != 0 (sort all next placed teams out) (DONE WITHOUT TESTING)

    # highest scoring next best placed teams
    x2 = a % len(groups)

    if x2 != 0:

        df = pd.DataFrame(columns=['P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'])

        for i in range(len(groups)):
            df = pd.concat([df, groups[i].head(1)])

        df = df.sort_values(['Pts', 'GD', 'GF', 'GA'], ascending=[False, False, False, True])
        idx2 = df.index.to_list()
        qualified_a.extend(idx2[:x2])

        # Now for qualified b (if % !=0) (Should be redundant in the World Cup, no use cases)
        if b != 0:
            del idx2[:x2]
            qualified_b.extend(idx2[:b])

    # Qualified b if % == 0

    if b !=0:

        y = math.floor(b / len(groups))

        for i in range(len(groups)):
            # Adding teams straight qualified to a list
            idx3 = groups[i].index.to_list()
            qualified_b.extend(idx3[:y])

    return qualified_a, qualified_b
