from stages.combined import worldcup_simulation
from functions.main_functions import choose_type, choose_num
from functions.presentation_functions import welcome

welcome()

sim_type, delay = choose_type()

sim_info = [sim_type, float(delay)]
sim_num = choose_num()

complete_data = worldcup_simulation(sim_info, sim_num)
