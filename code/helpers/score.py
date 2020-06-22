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

    # check the version thats neccesary, with efficient only last house added is checked, with no version all houses are checked
    if version == "efficient":

        # set house b as the last added house
        house_b = neighbourhood[-1]

        # loop through all the other houses
        for house_a in neighbourhood[:-1]:

            # check if houses is not water or the same as house b
            if house_a.name != "WATER" and house_b.name!="WATER": 
                if house_a != house_b:

                    # calculate minimum distance between the two houses
                    min_distance = distance_calculator(house_a,house_b)

                    # check if its less than saved minimum distances of the houses, if yes than new distances are saved as shortest distance
                    if house_a.shortest_distance > min_distance:
                        house_a.shortest_distance = min_distance
                    if house_b.shortest_distance > min_distance:
                        house_b.shortest_distance = min_distance
    else:

        # loop between all the houses with two for loops
        for house_a in neighbourhood:
            for house_b in neighbourhood:

                # check if houses is not water or the same as house b
                if house_a.name != "WATER" and house_b.name!="WATER": 
                    if house_a != house_b:

                        # calculate minimum distance between the two houses
                        min_distance = distance_calculator(house_a,house_b)

                        # check if its less than saved minimum distances of the houses, if yes than new distances are saved as shortest distance
                        if house_a.shortest_distance > min_distance:
                            house_a.shortest_distance = min_distance
                        if house_b.shortest_distance > min_distance:
                            house_b.shortest_distance = min_distance

    # return the neighbourhood with the updated distances
    return neighbourhood

def distance_calculator(house_a,house_b):

    # make a list
    distances= []

    # make a list with all the occupied grid places on x or y axis
    vert = list(range(house_a.y0, house_a.y1))
    horz = list(range(house_a.x0, house_a.x1))

    # check if house is on left or right side of house
    if house_b.y0 in vert or house_b.y1 in vert:
        distances += [abs(house_a.x0-house_b.x0),abs(house_a.x1-house_b.x0),abs(house_a.x0-house_b.x1),abs(house_a.x1-house_b.x1)]

    # check if house is above or below side of the house
    elif house_b.x0 in horz or house_b.x1 in horz:
        distances += [abs(house_a.y0-house_b.y0),abs(house_a.y1-house_b.y0),abs(house_a.y0-house_b.y1),abs(house_a.y1-house_b.y1)]

    else:
        # check if the shortest distance is diagonal
        if house_a.y1 <= house_b.y0:

            # upper right
            if house_a.x1 <= house_b.x0:
                distances += [distanceCalc(house_a.x1,house_a.y1,house_b.x0,house_b.y0)]

            # upper left
            else:
                distances += [distanceCalc(house_a.x0,house_a.y1,house_b.x1,house_b.y0)]
        elif house_a.y1 >= house_b.y0:

            # down right
            if house_a.x1 <= house_b.x0:
                distances += [distanceCalc(house_a.x1,house_a.y0,house_b.x0,house_b.y1)]

            # down left
            else:
                distances += [distanceCalc(house_a.x0,house_a.y0,house_b.x1,house_b.y1)]
                
    # get the minimum distance and return it
    return min(distances)