def choose_type():

    delay = 0

    while True:
        try:
            sim_type = int(input('\nChoose type of simulation, 0 = detailed, 1 = fast: '))

            if sim_type == 0 or sim_type == 1:
                break
            else:
                continue
        except:
            print("Don't be cheeky, enter 0 or 1: ")

    if sim_type == 0:

        delay = input('Choose your time delay for qualifying, 0 is recommended: ')

    return sim_type, delay

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

