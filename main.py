from stages.combined import worldcup_simulation
from functions.main_functions import choose_type, choose_num
from functions.presentation_functions import welcome
from functions.data_functions import post_data_update

welcome()

# functions to allow user to select parameters
data, sim_info = choose_type()
sim_num = choose_num()

# running the sim_num of World Cups and returning data
complete_data = worldcup_simulation(data, sim_info, sim_num)

complete_data = post_data_update(complete_data)

# saving data into app folder
complete_data[0].to_csv('app_data/complete_nation_data.csv')
complete_data[1].to_csv('app_data/complete_player_data.csv')

