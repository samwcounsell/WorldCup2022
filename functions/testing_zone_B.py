import pandas as pd

# p_df = pd.read_csv('poc.csv')

def reset():

    p_df = pd.read_csv('poc.csv')

    return p_df


def add_score_1():
    p_df.loc[1, 'Score'] = p_df.loc[1, 'Score'] + 1

    return p_df


def add_score_2():
    p_df.loc[0, 'Score'] = p_df.loc[0, 'Score'] + 2

    return p_df

p_df = reset()