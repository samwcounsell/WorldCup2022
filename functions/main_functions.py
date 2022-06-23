import pandas as pd


def choose_type():
# returns 2 lists of length 2, data and then sim_info,
# sim_info defines detail level of simulations and delay for the qualifiers

    # default delay is 0
    delay = 0

    nation_data, player_data = pd.read_csv('sim_data/nation_data.csv'), pd.read_csv(
        'sim_data/player_data.csv')

    while True:

        try:
            sim_type = int(input('\nChoose type of simulation, 0 = detailed, 1 = fast: '))

            if sim_type == 0 or sim_type == 1 or sim_type == 2:
                break

            else:
                continue

        except:
            print("Don't be cheeky, enter 0 or 1: ")

    if sim_type == 2:
        nation_data, player_data = pd.read_csv('sim_data/legends_nation_data.csv'), pd.read_csv('sim_data/legends_player_data.csv', engine = 'python')
        print("\nLegend mode enabled")
        sim_type = int(input('\nNow choose type of simulation, 0 = detailed, 1 = fast: '))

    if sim_type == 0:
        delay = input('Choose your time delay for qualifying, 0 is recommended: ')

    data = [nation_data, player_data]
    sim_info = [sim_type, float(delay)]

    return data, sim_info


def choose_num():
    while True:
        try:
            sim_num = int(input('\nChoose number of simulations: '))
            if sim_num > 0:
                break
            else:
                continue
        except:
            print("Don't be cheeky, enter an integer greater than zero: ")

    return sim_num
