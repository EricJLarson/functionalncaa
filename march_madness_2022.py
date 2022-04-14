import numpy as np

""" 2022 Men's NCAA Tournament Bracket """ 
bracket = [
    
    # West Region
    ('GONZ', 1),
    ('GAST', 16),
    
    ('BSU', 8),
    ('MEM', 9),
    
    ('CONN', 5),
    ('NMSU', 12),    
    
    ('ARK', 4),
    ('UVM', 13),
    
    ('ALA', 6),
    ('ND', 11),        

    ('TTU', 3),
    ('MTST', 14),        
    
    ('MSU', 7),
    ('DAV', 10),        
    
    ('DUKE', 2),
    ('CSUF', 15),    
    
 
    # East Region
    ('BAY', 1),
    ('NORF', 16),
    
    ('UNC', 8),
    ('MARQ', 9),
    
    ('SMC', 5),
    ('IU', 12),    
    
    ('UCLA', 4),
    ('ARK', 13),
    
    ('TEX', 6),
    ('VT', 11),        

    ('PUR', 3),
    ('YALE', 14),        
    
    ('MUR', 7),
    ('SF', 10),        
    
    ('UK', 2),
    ('SPU', 15),        


    # South Region
    ('ARIZ', 1),
    ('WSU', 16),
    
    ('HALL', 8),
    ('TCU', 9),
    
    ('HOU', 5),
    ('UAB', 12),    
    
    ('ILL', 4),
    ('UTC', 13),
    
    ('CSU', 6),
    ('MICH', 11),        

    ('TENN', 3),
    ('LONG', 14),        
    
    ('OSU', 7),
    ('LUC', 10),        
    
    ('VILL', 2),
    ('DEL', 15), 
    
    # Midwest Region
    ('KU', 1),
    ('TXS', 16),
    
    ('SDSU', 8),
    ('CREI', 9),
    
    ('IOWA', 5),
    ('RICH', 12),    
    
    ('PROV', 4),
    ('SDST', 13),
    
    ('LSU', 6),
    ('ISU', 11),        

    ('WISC', 3),
    ('COLG', 14),        
    
    ('USC', 7),
    ('MIA', 10),        
    
    ('AUB', 2),
    ('JVST', 15),     

]


""" Add noise to the prediction dependent on the tournament round (excluding FF and C) """
round_variation = {'R64': 0.025, 'R32': 0.05,  'SS': 0.075, 'E8': 0.1 , 'FF': 0.0, 'C': 0.0}


""" Determine the tournament round based on the number of remaining teams """
def get_tourney_round(bracket):
    num_remaining_teams = len(bracket)
    if num_remaining_teams == 64:
        tourney_round = 'R64'
    elif num_remaining_teams == 32:
        tourney_round = 'R32'
    elif num_remaining_teams == 16:
        tourney_round = 'SS'    
    elif num_remaining_teams == 8:
        tourney_round = 'E8'
    elif num_remaining_teams == 4:
        tourney_round = 'FF'
    elif num_remaining_teams == 2:
        tourney_round = 'C'
    
    return tourney_round


""" Simulate a single game """
def simulate_game(teamA, teamB, tourney_round):
    teams_playing = [teamA, teamB]
    seedA, seedB = teamA[1], teamB[1]
    seed_sum = seedA + seedB
    round_noise = np.random.uniform(0, round_variation.get(tourney_round))
    if tourney_round in ['R64', 'R32', 'SS', 'E8']:
    	# Determine the winner based on team seeding, favoring higher seeds, and adding noise based on the round.
        winning_probs = (seedB / seed_sum - round_noise, seedA / seed_sum + round_noise)
        winning_team_seed = np.random.choice([seedA, seedB], p = winning_probs)
        winning_team_tuple = [x for x in teams_playing if x[1] == winning_team_seed][0]
        losing_team_tuple = [x for x in teams_playing if x[1] != winning_team_seed][0]
    else: # FF or C
    	# Assign equal probabilities for the Final Four and Championship game
        winning_team_name = np.random.choice([teamA[0], teamB[0]])
        winning_team_tuple = [x for x in teams_playing if x[0] == winning_team_name][0]
        losing_team_tuple = [x for x in teams_playing if x[0] != winning_team_name][0]

    print(f'({winning_team_tuple[1]}) {winning_team_tuple[0]} defeats ({losing_team_tuple[1]}) {losing_team_tuple[0]}')
    
    return winning_team_tuple



""" Simulate one full bracket round """
def simulate_bracket(bracket):
    remaining_teams = []
    tourney_round = get_tourney_round(bracket)
    print(f'BEGINNING {tourney_round} \n')
    i = 0
    while i < len(bracket):
        team_one, team_two = bracket[i], bracket[i+1]
        winning_team = simulate_game(team_one, team_two, tourney_round)
        i += 2
        remaining_teams.append(winning_team) 
        if i % 2 == 0: # Add spacing for the tournament output    
            print()
    print('------------------------------------------------------------------ \n')            
    
    return remaining_teams


""" Simulate the entire tournament """
def simulate_march_madness(bracket):
    # Initialize the remaining teams to be the full bracket
    remaining_teams = bracket 

    while len(remaining_teams) > 1: 
        remaining_teams = simulate_bracket(remaining_teams)
    
    return remaining_teams



simulate_march_madness(bracket)
