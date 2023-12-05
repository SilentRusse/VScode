data = open("day 2 AoC\data.txt").read().split("\n")
#turn    
rock = 1 #'X' or 'A'
paper = 2 #'Y' or 'B'
sciccors = 3 #'Z' or 'C'
#outcome
win = 6
draw = 3
lose = 0
#list for points earned
points = []
turn = 0
for round in data:
    opponent, myself = round.split()
    if opponent == 'A':#rock
        if myself == 'X':
            turn = rock + draw
        elif myself == 'Y':
            turn = paper + win
        elif myself == 'Z':
            turn = sciccors + lose
        points.append(turn)

    elif opponent == 'B': #paper
        if myself == 'X':
            turn = rock + lose 
        elif myself == 'Y':
            turn = paper + draw
        elif myself == 'Z':
            turn = sciccors + win
        points.append(turn)

    elif opponent == 'C': #sciccors
        if myself == 'X':
            turn = rock + win
        elif myself == 'Y':
            turn = paper + lose
        elif myself == 'Z':
            turn = sciccors + draw
        points.append(turn)
print(f"Sum of all games:{sum(points)}")
points.clear()
for round in data:
    opponent, myself = round.split()
    if myself == 'X':#lose
        if opponent == 'A':
            turn = sciccors + lose
        elif opponent == 'B':
            turn = rock + lose
        elif opponent == 'C':
            turn = paper + lose
        points.append(turn)

    if myself == 'Y':#draw
        if opponent == 'A':
            turn = rock + draw
        elif opponent == 'B':
            turn = paper + draw
        elif opponent == 'C':
            turn = sciccors + draw
        points.append(turn) 

    if myself == 'Z':#win
        if opponent == 'A':
            turn = paper + win
        elif opponent == 'B':
            turn = sciccors + win
        elif opponent == 'C':
            turn = rock + win
        points.append(turn)
print(f"Sum of all games (Part 2):{sum(points)}")