"""
score.py

Wordt gebruikt om de score van een wijkindeling te berekenen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import math
from code.helpers.location import distanceCalc

def scorecalculator(neighbourhood):
    # set score to 0
    score = 0
    # loop through every item in the neighbourhood that's not water
    for house in neighbourhood:
        if house.name != "WATER":
            # calculate the new house price with the price increasement from the extra free space
            house.score = (house.price + house.price*house.price_increasement*(round_down(house.shortest_distance,0) - house.free_area))
            score += house.score
    # return the score
    return score

def round_down(n, decimals=0):
    # the selected decimals as a power of the 10 to get the decimals before the .
    multiplier = 10 ** decimals
    # math.floor rounds the number down to the closest whole number below, though the multiplier we keep the wanted decimals
    return math.floor(n * multiplier) / multiplier

def distance_check(neighbourhood, version="efficient"):
    if version == "efficient":
        house_b = neighbourhood[-1]
        for house_a in neighbourhood[:-1]:
            if house_a.name != "WATER" and house_b.name!="WATER": 
                if house_a != house_b:
                    min_distance = distance_calculator(house_a,house_b)
                    if house_a.shortest_distance > min_distance:
                        house_a.shortest_distance = min_distance
                    if house_b.shortest_distance > min_distance:
                        house_b.shortest_distance = min_distance
    else:
        for house_a in neighbourhood:
            for house_b in neighbourhood:
                if house_a.name != "WATER" and house_b.name!="WATER": 
                    if house_a != house_b:
                        min_distance = distance_calculator(house_a,house_b)
                        if house_a.shortest_distance > min_distance:
                            house_a.shortest_distance = min_distance
                        if house_b.shortest_distance > min_distance:
                            house_b.shortest_distance = min_distance
    return neighbourhood

def distance_calculator(house_a,house_b):
    distances= []
    vert = list(range(house_a.y0-1, house_a.y1+1))
    horz = list(range(house_a.x0-1, house_a.x1+1))
    if house_b.y0 in vert or house_b.y1 in vert:
        distances += [abs(house_a.x0-house_b.x0),abs(house_a.x1-house_b.x0),abs(house_a.x0-house_b.x1),abs(house_a.x1-house_b.x1)]
    elif house_b.x0 in horz or house_b.x1 in horz:
        distances += [abs(house_a.y0-house_b.y0),abs(house_a.y1-house_b.y0),abs(house_a.y0-house_b.y1),abs(house_a.y1-house_b.y1)]
    else:
        if house_a.y1 < house_b.y0:
            if house_a.x1 < house_b.x0:
                distances += [distanceCalc(house_a.x1,house_a.y1,house_b.x0,house_b.y0)]
            else:
                distances += [distanceCalc(house_a.x0,house_a.y1,house_b.x1,house_b.y0)]
        elif house_a.y1 > house_b.y0:
            if house_a.x1 < house_b.x0:
                distances += [distanceCalc(house_a.x1,house_a.y0,house_b.x0,house_b.y1)]
            else:
                distances += [distanceCalc(house_a.x0,house_a.y0,house_b.x1,house_b.y1)]
    return min(distances)