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

from code.helpers.score import scorecalculator, distance_check
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.classes.objects import Borders, House, Water
from code.helpers.location import location_checker
from code.helpers.performance import performanceplot

def greedy_algorithm(iterations, water_layout, max_houses):
    # standard neighbourhood distribution of the houses
    fraction_bungalow,fraction_maison = 0.25, 0.15
    amount_bungalow, amount_maison =  max_houses * fraction_bungalow, max_houses * fraction_maison
    highest_score, table = 0, []
    
    # create neighbourhood, place water and build houses, collect neighbourhood and score
    neighbourhood = []
    neighbourhood = waterbuilder(water_layout, neighbourhood)
    highest_score = 0
    bezet = []
    for i in neighbourhood:
        for j in range(i.x0, i.x1):
            for k in range(i.y0, i.y1):
                bezet += [(j,k)]

    # neighbourhood, score = greedy_housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)
    for i in range(max_houses):
        highest_score = 0
        if i < amount_maison:
            test_house = House("maison", i)
            name = "maison"
        elif i < amount_maison + amount_bungalow:
            test_house = House("bungalow", i)
            name = "bungalow"
        else:
            test_house = House("sfh", i)
            name = "sfh"
        lijst = []
        for a in range(test_house.free_area, (Borders().maxX - test_house.free_area - test_house.width)):
            for b in range(test_house.free_area, (Borders().maxY - test_house.free_area - test_house.width)):
                if (a,b) not in bezet:
                    lijst += [(a,b)]
        for plek in lijst:
            a = plek[0]
            b = plek[1]
            temp_neighbourhood = deepcopy(neighbourhood)
            if name == "maison":
                house = House("maison", i,a,b)
                if location_checker(house, temp_neighbourhood) == True:
                    temp_neighbourhood.append(house)
                    temp_neighbourhood = distance_check(temp_neighbourhood)
                    new_score = scorecalculator(temp_neighbourhood)
                    if new_score > highest_score:
                        best_house = deepcopy(house)
                        highest_score = new_score
            elif name == "bungalow":
                house= House("bungalow",i, a, b)
                if location_checker(house, temp_neighbourhood) == True:
                    temp_neighbourhood.append(house)
                    temp_neighbourhood = distance_check(temp_neighbourhood)
                    new_score = scorecalculator(temp_neighbourhood)
                    if new_score > highest_score:
                        best_house = deepcopy(house)
                        highest_score = new_score
            elif name == "sfh":
                house = House("sfh",i,a,b)
                if location_checker(house, temp_neighbourhood) == True:
                    temp_neighbourhood.append(house)
                    temp_neighbourhood = distance_check(temp_neighbourhood)
                    new_score = scorecalculator(temp_neighbourhood)
                    if new_score > highest_score:
                        best_house = deepcopy(house)
                        highest_score = new_score
        
        neighbourhood.append(best_house)
        for i in range(best_house.x0,best_house.x1):
            for j in range(best_house.y0, best_house.y1):
                bezet += [(i,j)]
        neighbourhood = distance_check(neighbourhood)
        score = scorecalculator(neighbourhood)
        table.append([i, max_houses, score])

    # save the information from the iteration
    df_greedy = pd.DataFrame(table, columns = ["iteration", "max_houses","score"])
    df_greedy.to_csv("results/"+ str(iterations)+"-"+str(max_houses)+"-greedy.csv")
    
    # make a visualisation of the best random neighbourhood and save it
    visualise(neighbourhood, highest_score, "greedy_visualisation-" + str(max_houses))

    # make a histogram of the scores from all the neighbourhoods made through the iterations
    performanceplot("Greedy", max_houses, "line", df_greedy.iteration, df_greedy.score)

    return neighbourhood, score