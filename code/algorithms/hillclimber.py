"""
hill climber
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd

from copy import deepcopy

from code.helpers.score import scorecalculator
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.classes.objects import *

def hillclimber_algorithm(iterations, water_layout, max_houses):

    ################################ start by creating a random neighbourhood ###################
    
    # standard neighbourhood distribution of the houses
    amount_sfh, amount_bungalow, amount_maison = max_houses*0.6, max_houses*0.25, max_houses*0.15

    # create neighbourhood, place water and build houses, collect neighbourhood and score
    neighbourhood = []
    neighbourhood = waterbuilder(water_layout, neighbourhood)
    neighbourhood, score = housebuilder(max_houses, amount_maison, amount_bungalow, amount_sfh, neighbourhood)
    
    ################################ now iterate using the hill climber method ####################

    # for loop through iterations
    for i in range(iterations):

        # create a deepcopy of the current neighbourhood layout
        temp_neighbourhood = deepcopy(neighbourhood)

        # choose a random house
        random_house = rd.choice(temp_neighbourhood)

        # choose a random new location for this house
        random_house.x = rd.randrange(random_house.free_area, (Borders().maxX - random_house.free_area - random_house.width))
        random_house.y = rd.randrange(random_house.free_area, (Borders().maxY - random_house.free_area - random_house.width))

        # use location checker to check whether it is allowed to place the house here
        if location_checker(random_house, temp_neighbourhood) == False:
            break

        # if OK, place the house on this new location

        # now calculate the score of this new neighbourhood
        new_score = scorecalculator(temp_neighbourhood)

        # compare the score of the old neighbourhood to the new one, choose the best one
        if new_score > score:
            score = new_score

    # make a visualisation of the best score and save it
    visualise(neighbourhood, score, "hillclimber")
