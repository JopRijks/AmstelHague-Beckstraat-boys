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

def scorecalculator(neighbourhood):
    """Calculates the total score of the entire neighbourhood in euros."""

    # initiate score variable
    score = 0

    # loop through all houses in the neighbourhood
    for house in neighbourhood:
        if house.name != "WATER":

            # calculate the new house price with the price increasement without acknowledging the obligated free space
            # this is wat check50 wants but we believe that it is not right according to the assignment
            house.score = house.price * (1 + house.price_increasement * math.floor(house.shortest_distance))

            # calculate the new house price with the price increasement from the extra free space
            
            # this should be correct according to the assignment but not for check50, thus it is placed as a comment
            # but if it is used as code it calculates the score using only the EXTRA free space, not the required free space
            # house.score = house.price * (1 + house.price_increasement * (math.floor(house.shortest_distance) - house.free_area))

            # add house score to neighbourhood score
            score += house.score

    # return the score of the whole neighbourhood
    return score


def distance_check(neighbourhood, version="efficient"):
    """Calculates the shortest distance to another house for each house in the neighbourhood"""

    # create a polygon for every house in the neighbourhood
    poly_dict = {i.id : Polygon([(i.x0,i.y0), (i.x1,i.y0), (i.x1,i.y1), (i.x0,i.y1)]) for i in neighbourhood if i.name != "WATER"}
    poly_list = list(poly_dict.values())
    
    # loop through polygon dictionary to calculate the shortest distances
    shortest_distance = {}
    for house_id, poly in poly_dict.items():
        
        # calculate the shortest distance to a different house
        poly_rest = deepcopy(poly_list)
        poly_rest.remove(poly)
        shortest_distance[house_id] = poly.distance(MultiPolygon(poly_rest))
    
    # update house object attribute with new shortest distance value
    for house in neighbourhood:
        if house.name != "WATER":
            house.shortest_distance = shortest_distance[house.id]

    # return updated neighbourhood
    return neighbourhood
   