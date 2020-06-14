import math

def scorecalculator(neighbourhood):
    score = 0
    for house in neighbourhood:
        if house.name != "WATER":
            score = score +house.price + house.price*(round_down(house.shortest_distance,0) - house.free_area)*house.price_increasement
    return score

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

