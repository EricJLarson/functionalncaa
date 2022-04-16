import bracket
import numpy as np

"""
 Each GAME is represented by a tuple: (WINNER,(HISTORY_A, HISTORY_B)), where each HISTORY 
 is composed of a GAME.

 A WINNER is a TEAM. 
 A TEAM is a tuple: (NAME, SEED).
"""

# winner
def w(game): return game[0]

# History
def h(game): return game[1]

# seed
def s(team): return team[1]

# name 
def n(team): return team[0]

def depth(game):
    return 0 if len(game) == 1 else depth(h(game)[0]) + 1

def determineWinner(teamA, teamB, depth):
    roundVariation = (depth + 1) * 0.25 if depth  < 4 else 0.0
    noise = np.random.uniform(0, roundVariation)
    seedSum = s(teamA) + s(teamB)
    noise = min(noise, s(teamA)/seedSum , s(teamB)/seedSum)
    probs = (
        s(teamA) / seedSum - noise, 
        s(teamB) / seedSum + noise
    ) 
    index = np.random.choice(2, p = probs)
    return teamB if index == 0 else teamA

def game(gameA, gameB):
    winner = determineWinner(w(gameA), w(gameB), depth(gameA)) 
    history = (gameA, gameB)
    return (winner, history)

def simulate(bracket):  
    if len(bracket) == 2:
        return game(bracket[0], bracket[1])
    else:
        middle = len(bracket)//2
        left = bracket[:middle]
        right = bracket[middle:]
        return simulate((simulate(left), simulate(right)))

bracket22 = bracket.bracket 
# Convert each TEAM to a GAME with an emtpy HISTORY
initial_games = [ (team,) for team in bracket22 ]
results = simulate(initial_games)

"""
Examples of querying the results
"""

def find(game, name):
    if len(game) == 1:
        return 0
    if (w(game)[0]) == name:
        return depth(game) 
    return max(find(h(game)[0], name), find(h(game)[1], name) )

def getFind(game):
    return lambda name: find(game, name)

print(f'Winner {w(results)}')
aub = find(results, "AUB")
print(f'AUB level: {aub}')

def getResults(results):
    findFinal = getFind(results)
    team2result = [ (n(team), s(team), findFinal(n(team))) for team in bracket22 ]
    team2result.sort(key = lambda x: x[2]) 
    team2resultStr = '\n'.join([ f'{n(result)},{s(result)}, {result[2]}' for result in team2result ])
    return team2resultStr

team2resultStr = getResults(results)
print(f'\n\nTEAM,SEED,LEVEL\n---------\n{team2resultStr}')

