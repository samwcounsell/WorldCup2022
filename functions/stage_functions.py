from functions.group_stage import group_draw, group_simulation


def group_stage(group_number, group_size, legs, number_of_teams_to_progress):

    groups = group_draw(group_number, group_size)

    for i in range(group_number):
        teams = groups[i]
        groups[i] = group_simulation(teams, legs)

    # TODO: add function that decides which teams go through
    # use modulo function, so if 18 teams go through from 8 groups do floor(18/8) = 2
    # so top two teams go through, then do 18%8 = 2, and select two best third place teams go through

# def knockout():
