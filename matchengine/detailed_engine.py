from scipy.stats import bernoulli
from functions.match_day_functions import match_data_collection, detailed_sim_goal, commentary

import time


# single_sim_match runs the whole match as part of a detailed World Cup simulations
def detailed_sim_match(data, participants, WC, sim_info):
    # run match_data_retrieval here
    # import not required
    # return p_home, p_away, player_lists and their ratings

    nation_df, player_df = data[0], data[1]
    home, away = participants[0], participants[1]

    # TODO: Add proper match introduction
    print(f"\n{home} v {away}:")

    p_home, home_players, home_atk, home_pass, p_away, away_players, away_atk, away_pass = match_data_collection(
        data, participants)

    # Running binomial simulation with size 90
    if sim_info[0] < 2:

        score_home, score_away = 0, 0

        for m in range(90):
            time.sleep(sim_info[1])
            min_score = [bernoulli.rvs(p_home, size=1), bernoulli.rvs(p_away, size=1)]
            score_home, score_away = score_home + min_score[0], score_away + min_score[1]
            if sum(min_score) > 0:
                detailed_sim_goal(sim_info, m, min_score, [score_home, score_away], data[1], home, home_players, home_atk, home_pass, away, away_players, away_atk, away_pass,
                            WC)

    # For knockout matches ET
    if sim_info[0] > 1:

        score_home, score_away = 0, 0

        for m in range(30):
            time.sleep(sim_info[1])
            min_score = [bernoulli.rvs(p_home, size=1), bernoulli.rvs(p_away, size=1)]
            score_home, score_away = score_home + min_score[0], score_away + min_score[1]
            if sum(min_score) > 0:
                detailed_sim_goal(sim_info, m, min_score, [score_home, score_away], data[1], home, home_players, home_atk, home_pass, away, away_players, away_atk, away_pass,
                            WC)

    # Calculate scorers and assisters
    detailed_sim_nation_events(nation_df, home, away, score_home, score_away, WC)
    detailed_sim_player_events(player_df, home, away, WC)

    data = [nation_df, player_df]
    score = [score_home, score_away]

    return data, score


def detailed_sim_nation_events(nation_df, home, away, score_home, score_away, WC):
    # Updating the nation sim_data after the game

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
def detailed_sim_player_events(player_df, home, away, WC):

    player_df.loc[player_df['Country'] == home, 'P'] = player_df.loc[player_df['Country'] == home, 'P'] + 1
    if WC > 0:
        player_df.loc[player_df['Country'] == home, 'WC_P'] = player_df.loc[
                                                                  player_df['Country'] == home, 'WC_P'] + 1

    player_df.loc[player_df['Country'] == away, 'P'] = player_df.loc[player_df['Country'] == away, 'P'] + 1
    if WC > 0:
        player_df.loc[player_df['Country'] == away, 'WC_P'] = player_df.loc[
                                                                  player_df['Country'] == away, 'WC_P'] + 1
