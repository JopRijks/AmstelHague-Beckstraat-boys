"""
hillclimber.py

Wordt voor het hill climber algoritme gebruikt om met een aantal iteraties de hill climber methode toe te passen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd

from copy import deepcopy

from code.helpers.score import scorecalculator, distance_check
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.helpers.location import location_checker
from code.classes.objects import Borders, House
from code.helpers.performance import performanceplot

def hillclimber_algorithm(iterations, water_layout, max_houses, neighbourhood=None, score = None):

    ################################ start by creating a random neighbourhood ###################
    
    # standard neighbourhood distribution of the houses
    amount_sfh, amount_bungalow, amount_maison = max_houses*0.6, max_houses*0.25, max_houses*0.15

    if neighbourhood != None:
        file_name = "greedy-hilclimber"
    else:
        file_name = "hillclimber"

    # create table
    table = []
    if neighbourhood == None:
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
        random_house = rd.choice([h for h in temp_neighbourhood if h.name != "WATER"])
        temp_neighbourhood.remove(random_house)
        
        # get house type and id
        type_house = random_house.type
        ID = random_house.id

        # make house with same id and type
        house = House(type_house,str(ID))
        if location_checker(house, temp_neighbourhood) == False:
            while location_checker(house, temp_neighbourhood) == False:
                house = House(type_house, i)
        
        temp_neighbourhood.append(house)

        # calculate new shortest_distances
        temp_neighbourhood = distance_check(temp_neighbourhood)

        # now calculate the score of this new neighbourhood
        new_score = scorecalculator(temp_neighbourhood)

        # compare the score of the old neighbourhood to the new one, choose the best one
        if new_score > score:
            neighbourhood = deepcopy(temp_neighbourhood)
            score = new_score

        # save progress in table
        table.append([i, max_houses, score, new_score])

    # save results in csv file
    df_hillclimber = pd.DataFrame(table, columns = ["iteration", "max_houses", "old_score", "new_score"])
    df_hillclimber.to_csv("results/" + str(iterations) + "-" + str(max_houses) +"-" + file_name +".csv")

    # make a visualisation of the best score and save it
    visualise(neighbourhood, score, file_name+"_visualisation-"+str(max_houses))
    
    # create a plot of the progress
    performanceplot(file_name, max_houses, "line", df_hillclimber.iteration, df_hillclimber.old_score)

    return neighbourhood, score