from scipy.stats import bernoulli
from functions.match_day_functions import match_data_collection

import random


# multi_sim_match runs the whole match as part of multiple World Cup simulations
def multi_sim_match(data, participants, WC):
    # run match_data_retrieval here
    # import not required
    # return p_home, p_away, player_lists and their ratings

    nation_df, player_df = data[0], data[1]
    home, away = participants[0], participants[1]

    p_home, home_players, home_atk, home_pass, p_away, away_players, away_atk, away_pass = match_data_collection(
        nation_df, player_df, home,
        away)

    # Running binomial simulation with size 90
    score_home, score_away = sum(bernoulli.rvs(p_home, size = 90)), sum(bernoulli.rvs(p_away, size = 90))

    # Calculate scorers and assisters
    multi_sim_nation_events(nation_df, home, away, score_home, score_away, WC)
    multi_sim_player_events(player_df, score_home, home_players, home_atk, home_pass, score_away,
                            away_players, away_atk, away_pass, WC)

    # Printing the match result (Replace this with post_match later)
    print(f"\nFinal Score: {home} {score_home} - {score_away} {away}")

    data = [nation_df, player_df]
    score = [score_home, score_away]

    return(data, score)


def multi_sim_nation_events(nation_df, home, away, score_home, score_away, WC):
    # Updating the nation data after the game

    nation_df.loc[nation_df['Country'].isin([home, away]), 'P'] = nation_df.loc[
                                                                   nation_df['Country'].isin([home, away]), 'P'] + 1

    if WC > 0:
        nation_df.loc[nation_df['Country'].isin([home, away]), 'WC_P'] = nation_df.loc[
                                                                          nation_df['Country'].isin([home,
                                                                                                   away]), 'WC_P'] + 1

    # home
    nation_df.loc[nation_df['Country'] == home, 'GF'] = nation_df.loc[nation_df['Country'] == home, 'GF'] + score_home
    nation_df.loc[nation_df['Country'] == home, 'GA'] = nation_df.loc[nation_df['Country'] == home, 'GA'] + score_away

    if WC > 0:
        nation_df.loc[nation_df['Country'] == home, 'WC_GF'] = nation_df.loc[
                                                                   nation_df['Country'] == home, 'WC_GF'] + score_home
        nation_df.loc[nation_df['Country'] == home, 'WC_GA'] = nation_df.loc[
                                                                   nation_df['Country'] == home, 'WC_GA'] + score_away

    if away == 0:
        nation_df.loc[nation_df['Country'] == home, 'Clean_Sheets'] = nation_df.loc[nation_df[
                                                                                        'Country'] == home, 'Clean_Sheets'] + 1

    # away
    nation_df.loc[nation_df['Country'] == away, 'GF'] = nation_df.loc[nation_df['Country'] == away, 'GF'] + score_away
    nation_df.loc[nation_df['Country'] == away, 'GA'] = nation_df.loc[nation_df['Country'] == away, 'GA'] + score_home

    if WC > 0:
        nation_df.loc[nation_df['Country'] == away, 'WC_GF'] = nation_df.loc[
                                                                   nation_df['Country'] == away, 'WC_GF'] + score_away
        nation_df.loc[nation_df['Country'] == away, 'WC_GA'] = nation_df.loc[
                                                                   nation_df['Country'] == away, 'WC_GA'] + score_home

    if home == 0:
        nation_df.loc[nation_df['Country'] == away, 'Clean_Sheets'] = nation_df.loc[nation_df[
                                                                                        'Country'] == away, 'Clean_Sheets'] + 1


# Calculates detail of main player events i.e., goals for a multi_sim_match
def multi_sim_player_events(player_df, home, home_players, home_atk, home_pass, away, away_players, away_atk, away_pass,
                            WC):
    #print(home_players, away_players)
    #print(home_pass, away_pass)

    # Updating the player data after the game
    for i in range(home):
        scorer = random.choices(home_players, weights=home_atk, k=1)[0]
        index = home_players.index(scorer)
        player_df.loc[player_df['Name'] == scorer, 'Goals'] = player_df.loc[player_df['Name'] == scorer, 'Goals'] + 1
        if WC > 0:
            player_df.loc[player_df['Name'] == scorer, 'WC_Goals'] = player_df.loc[
                                                                         player_df['Name'] == scorer, 'WC_Goals'] + 1

        # TODO: Works up until here, needs to fix .loc error

        x = random.uniform(0, 10)
        if x < 8:
            possible_assisters = home_players[:]
            possible_assisters.pop(index)
            possible_weights = home_pass[:]
            possible_weights.pop(index)
            assister = (random.choices(possible_assisters, weights=possible_weights, k=1))[0]
            player_df.loc[player_df['Name'] == assister, 'Assists'] = player_df.loc[
                                                                          player_df['Name'] == assister, 'Assists'] + 1
            if WC > 0:
                player_df.loc[player_df['Name'] == assister, 'WC_Assists'] = player_df.loc[player_df[
                                                                                               'Name'] == assister, 'WC_Assists'] + 1

    for j in range(away):
        scorer = (random.choices(away_players, weights=away_atk, k=1))[0]
        player_df.loc[player_df['Name'] == scorer, 'Goals'] = player_df.loc[player_df['Name'] == scorer, 'Goals'] + 1
        if WC > 0:
            player_df.loc[player_df['Name'] == scorer, 'WC_Goals'] = player_df.loc[
                                                                         player_df['Name'] == scorer, 'WC_Goals'] + 1

        x = random.uniform(0, 10)
        if x < 8:
            assister = (random.choices(away_players, weights=away_pass, k=1))[0]
            player_df.loc[player_df['Name'] == assister, 'Assists'] = player_df.loc[
                                                                          player_df['Name'] == assister, 'Assists'] + 1
            if WC > 0:
                player_df.loc[player_df['Name'] == assister, 'WC_Assists'] = player_df.loc[player_df[
                                                                                               'Name'] == assister, 'WC_Assists'] + 1

    player_df.loc[player_df['Country'] == home, 'P'] = player_df.loc[player_df['Country'] == home, 'P'] + 1
    if WC > 0:
        player_df.loc[player_df['Country'] == home, 'WC_P'] = player_df.loc[
                                                                  player_df['Country'] == home, 'WC_P'] + 1

    player_df.loc[player_df['Country'] == away, 'P'] = player_df.loc[player_df['Country'] == away, 'P'] + 1
    if WC > 0:
        player_df.loc[player_df['Country'] == away, 'WC_P'] = player_df.loc[
                                                                  player_df['Country'] == away, 'WC_P'] + 1
# Variable Glossary
# home/away - the two teams playing the match
# p_home/p_away - probability of home/away team scoring each minute
# score_home/score away - number of goals scored in the match by home/away team
