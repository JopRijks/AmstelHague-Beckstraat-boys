import math

def scorecalculator(neighbourhood):
    # set score to 0
    score = 0

    # loop through every item in the neighbourhood that's not water
    for house in neighbourhood:
        if house.name != "WATER":
            
            # calculate the new house price with the price increasement from the extra free space
            score += house.price + house.price*(round_down(house.shortest_distance,0) - house.free_area)*house.price_increasement
    # return the score
    return score

def round_down(n, decimals=0):
    # the selected decimals as a power of the 10 to get the decimals before the .
    multiplier = 10 ** decimals
    # math.floor rounds the number down to the closest whole number below, though the multiplier we keep the wanted decimals
    return math.floor(n * multiplier) / multiplier

