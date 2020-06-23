"""
greedy.py

Wordt voor het greedy algoritme gebruikt om volgens de greedy methode een wijk in te delen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy
import time

from code.helpers.score import scorecalculator, distance_check
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.classes.objects import Borders, House, Water
from code.helpers.location import location_checker
from code.helpers.performance import performanceplot

def greedy_algorithm(iterations, water_layout, max_houses, ts):
    # standard neighbourhood distribution of the houses
    fraction_bungalow,fraction_maison = 0.25, 0.15
    amount_bungalow, amount_maison =  max_houses * fraction_bungalow, max_houses * fraction_maison
    highest_score, table = 0, []
    
    # create neighbourhood, place water and build houses, collect neighbourhood and score
    neighbourhood = []
    neighbourhood = waterbuilder(water_layout, neighbourhood)
    highest_score = 0

    # make a bezet list with all the coordinates that are occupied with water
    bezet = []
    for i in neighbourhood:
        for j in range(i.x0, i.x1):
            for k in range(i.y0, i.y1):
                bezet += [(j,k)]

   # loop through the amount of houses
    for i in range(max_houses):

        # set higest score for house to 0
        highest_score = 0

        # house selector, get test house for values like free area, width and height
        if i < amount_maison:
            test_house = House("maison", i)
            name = "maison"
        elif i < amount_maison + amount_bungalow:
            test_house = House("bungalow", i)
            name = "bungalow"
        else:
            test_house = House("sfh", i)
            name = "sfh"

        # loop throug all coordinates and check if it's not in bezet
        for a in range(test_house.free_area, (Borders().maxX - test_house.free_area - test_house.width)):
            for b in range(test_house.free_area, (Borders().maxY - test_house.free_area - test_house.width)):
                if (a,b) not in bezet:

                    # get a deepcopy of neighbourhood
                    temp_neighbourhood = deepcopy(neighbourhood)

                    # make a house with the needed type on fixed coordinates
                    house = House(name, i,a,b)

                    # if it doesn't violates any rules add the house to the temporary neighbourhood
                    if location_checker(house, temp_neighbourhood) == True:
                        temp_neighbourhood.append(house)

                        # do a distance check and calculate the new score
                        temp_neighbourhood = distance_check(temp_neighbourhood)
                        new_score = scorecalculator(temp_neighbourhood)

                        # check if this score is the highest till now, if yes than save the house and score
                        if new_score > highest_score:
                            best_house = deepcopy(house)
                            highest_score = new_score
        
        # add the best house to the neighbourhood
        neighbourhood.append(best_house)

        # update bezet lijst with the values from best house
        for k in range(best_house.x0,best_house.x1):
            for l in range(best_house.y0, best_house.y1):
                bezet += [(k,l)]

        # do a distance check and calculate the new score        
        neighbourhood = distance_check(neighbourhood)
        score = scorecalculator(neighbourhood)

        # add a new row wiith values to the table
        table.append([i, max_houses, score])
    
    # create dataframe to plot algorithm performance
    df_greedy = pd.DataFrame(table, columns = ["iteration", "max_houses","score"])
    
    # make a visualisation of the best random neighbourhood and save it
    visualise(neighbourhood, highest_score, ts, "greedy_map-" + str(max_houses))

    # make a histogram of the scores from all the neighbourhoods made through the iterations
    performanceplot("Greedy", 1, max_houses, ts, df_greedy.iteration, df_greedy.score)

    return neighbourhood, score