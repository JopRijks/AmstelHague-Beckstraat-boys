"""
score.py

Wordt gebruikt om de score van een wijkindeling te berekenen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import math
from shapely.geometry import Polygon, MultiPolygon
from copy import deepcopy

from code.helpers.location import distanceCalc

def scorecalculator(neighbourhood):

    # initiate score variable
    score = 0

    # loop through all houses in the neighbourhood
    for house in neighbourhood:
        if house.name != "WATER":

            # calculate the new house price with the price increasement from the extra free space
            house.score = house.price * (1 + house.price_increasement * math.floor(house.shortest_distance))

            # add house score to neighbourhood score
            score += house.score

    # return the score of the whole neighbourhood
    return score


def distance_check(neighbourhood, version="efficient"):
    # initiate dictionaries
    houses_dict = {}
    shortest_distance = {}

    # loop through all houses in the neighbourhood
    for i in neighbourhood:
        if i.name != "WATER":

            # make a polygon using the corners of the house and add the polygon to the houses dictionary with as key the ID
            houses_dict[i.id] = Polygon([(i.x0,i.y0), (i.x1,i.y0), (i.x1,i.y1), (i.x0,i.y1)])
           
    # make a list of all the house values
    houses_list = list(houses_dict.values())
    
    # loop through all the houses dictionary
    for i, poly in houses_dict.items():
        
        # remove the house from the neighbourhood and get the distance from the house
        neighbourhood_rest = deepcopy(houses_list)
        neighbourhood_rest.remove(poly)
        shortest_distance[i] = poly.distance(MultiPolygon(neighbourhood_rest))
    
    # loop through the neighbourhood and update shortest distance
    for house in neighbourhood:
        if house.name != "WATER":
            house.shortest_distance = shortest_distance[house.id]

    # return updated neighbourhood
    return neighbourhood
   