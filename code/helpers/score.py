"""
score.py

Wordt gebruikt om de score van een wijkindeling te berekenen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import math
from shapely.geometry import Polygon, MultiPolygon

from code.helpers.location import distanceCalc

def scorecalculator(neighbourhood):

    # set score to 0
    score = 0

    # loop through every item in the neighbourhood that's not water
    for house in neighbourhood:
        if house.name != "WATER":

            # calculate the new house price with the price increasement from the extra free space
            house.score = house.price*(1 + house.price_increasement*(round_down(house.shortest_distance,0) - house.free_area))
            score += house.score

    # return the score
    return score

def round_down(n, decimals=0):

    # the selected decimals as a power of the 10 to get the decimals before the .
    multiplier = 10 ** decimals

    # math.floor rounds the number down to the closest whole number below, though the multiplier we keep the wanted decimals
    return math.floor(n * multiplier) / multiplier

def distance_check(neighbourhood, version="efficient"):
    # create dictionaries
    houses = {}
    shortest_distance = {}

    # loop through every house in the neighbourhood
    for i in neighbourhood:

        # check if house is not water
        if i.name != "WATER":

            # make a polygon of the house corners
            Polygon_House = Polygon([(i.x0,i.y0),(i.x0,i.y1),(i.x1,i.y0),(i.x1,i.y1)])
            
            # add the polygon to the houses dictionary with as key the ID
            houses[i.id] = Polygon_House
    
    # make a list of all the house values
    poly_houses = list(houses.values())
    
    # loop trhough all the houses dictionary
    for ID, House in houses.items():
        
        # remove the house from the neighbourhood and get the distance from the house
        rest_of_neighbourhood = list(poly_houses).remove(House)
        shortest_distance[ID] = float(House.distance(MultiPolygon(rest_of_neighbourhood)))
    
    # loop through the neighbourhood and update shortest distance
    for i in neighbourhood:
        if i.name != "WATER":
            if i.shortest_distance > shortest_distance[i.id]:
                i.shortest_distance = shortest_distance[i.id]
    
    return neighbourhood
   