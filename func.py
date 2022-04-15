import numpy as np

"""
 Each GAME is represented by a tuple: (WINNER,(HISTORY_A, HISTORY_B)), where each HISTORY 
 is composed of a GAME.

 A WINNER is a TEAM. 
 A TEAM is a tuple: (NAME, SEED).
"""

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
]

# winner
def w(a): 
    return a[0]

# seed
def s(a): 
    return a[1]

# History
def h(game):
    return game[1]

def depth(game):
    if len(game) == 1:
        return 0
    return depth(h(game)) + 1

# Takes two GAMEs 
def game(a,b):
    depth(a)
    return (w(a) if s(w(a)) < s(w(b)) else w(b), (a, b))

def simulate(bracket):  
    if len(bracket) == 2:
        return game(bracket[0], bracket[1])
    else:
        middle = len(bracket)//2
        left = bracket[:middle]
        right = bracket[middle:]
        return simulate((simulate(left), simulate(right)))

# Convert each TEAM to a GAME with an emtpy HISTORY
initial_games = [ (team,) for team in bracket ]

tournament = simulate(initial_games)

def find(game, name):
    if len(game) == 1:
        return 0
    if (w(game)[0]) == name:
        return depth(game) 
    return max(find(h(game)[0], name), find(h(game)[1], name) )

find(tournament, 'BSU')





depth(tournament)

depth((bracket[3],))

len((bracket[3],))














simulate(bracket[x:y])



brackethold = bracket


x = 0    
y = 4
bracket[x:y]
simulate(bracket[x:y])

len(((bracket[0],), (bracket[1],)))

game(bracket[0], bracket[1])

game((bracket[0],), (bracket[1],))

bracket[2:4]

def simulate(bracket):  
    if len(bracket) == 2:
        game(bracket[0], bracket[1])
    else:
        middle = len(bracket)//2
        left = bracket[:middle]
        right = bracket[middle:]
        return simulate((simulate(left), simulate(right)))


middle = len(bracket)//2

bracket[:middle]

bracket[middle:]

