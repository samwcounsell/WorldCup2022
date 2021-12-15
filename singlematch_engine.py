from scipy.stats import bernoulli

# Gives probability each team scores with every Bernoulli trial (each minute)
p_home, p_away = 0.014, 0.014

# Runs match from the singlematch_engine (slower but more detailed)
def singlematch(p_home, p_away):

    # Resetting the scores before the start of the match
    score_home, score_away = 0, 0

    # Running the minute function 90 times
    for i in range(90):

        # Retrieving whether a team scored in the previous minute and adding it to the total
        minute_home, minute_away = minute(p_home, p_away)
        score_home, score_away = score_home + minute_home, score_away + minute_away

    # Printing the match result (Replace this with post_match later)
    print(f"\nFinal Score: {' '.join(map(str, score_home))} - {' '.join(map(str, score_away))}")

    # Other functions to add
        # pre_match, post_match

# Calculates what happens in any given minute
def minute(p_home, p_away):

    # Runs a Bernoulli trial (i.e., weighted coin toss) to decide whether each team scored
    ber_home, ber_away = bernoulli.rvs(p_home, size=1), bernoulli.rvs(p_away, size=1)

    # Other functions to add
        # commentary, goal

    return ber_home, ber_away


# Running the match simulation
singlematch(p_home, p_away)



# Notes for Sam:
# For goalscorers (sme), pass list of players in match into minute, have match compile list of goalscorers,
# add goals from list to df post match