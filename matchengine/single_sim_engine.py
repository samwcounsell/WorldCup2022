from scipy.stats import bernoulli

# single_sim_match runs the whole match as part of one World Cup simulation
def single_sim_match(home, away):

    # run match_data_retrieval here
        # import not required
        # return p_home, p_away, player_lists and their ratings

    # run pre_match here

    # Resetting the scores before the start of the match
    score_home, score_away = 0, 0

    # Running the minute function 90 times
    for i in range(90):
        # Retrieving whether a team scored in the previous minute and adding it to the total
        minute_home, minute_away = minute(p_home, p_away)
        score_home, score_away = score_home + minute_home, score_away + minute_away

    # Printing the match result (Replace this with post_match later)
    print(f"\nFinal Score: {' '.join(map(str, score_home))} - {' '.join(map(str, score_away))}")

    # run post_match here


# calculates what happens in any given minute of a single_sim_match
def minute(p_home, p_away):

    # Runs a Bernoulli trial (i.e., weighted coin toss) to decide whether each team scored
    ber_home, ber_away = bernoulli.rvs(p_home, size=1), bernoulli.rvs(p_away, size=1)

    # Other functions to add
        # commentary, goal

    return ber_home, ber_away


# calculates detail of main events i.e., goals for a multi_sim_match
def single_sim_event():
    # import player_lists and their ratings
    # return scorers/assisters

    # Calculate goalscorers
    # Calculate assisters

    # Provide commentary



# Variable Glossary
# home/away - the two teams playing the match
# p_home/p_away - probability of home/away team scoring each minute
# score_home/score away - number of goals scored in the match by home/away team
# ber_home/ber_away - 0 or 1 depending on whether team scored in that minute