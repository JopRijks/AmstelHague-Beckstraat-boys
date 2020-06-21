"""
random.py

Wordt voor het random algoritme gebruikt om tot een willekeurige oplossing te komen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

from code.helpers.score import scorecalculator, distance_check
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.helpers.performance import performanceplot

def random_algorithm(iterations, water_layout, max_houses):
    
    # standard neighbourhood distribution of the houses
    fraction_sfh,fraction_bungalow,fraction_maison = 0.6, 0.25, 0.15
    amount_sfh, amount_bungalow, amount_maison = max_houses * fraction_sfh, max_houses * fraction_bungalow, max_houses * fraction_maison

    highest_score, best, table = 0, 0, []
    
    # performe the algorithm for a number of iterations
    for i in range(iterations):
        
        # create neighbourhood, place water and build houses, collect neighbourhood and score
        neighbourhood = []
        neighbourhood = waterbuilder(water_layout, neighbourhood)
        neighbourhood, score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)

        # if the score of the neighbourhood in this iteration is the highest till now than save the neighbourhood and the score
        if score > highest_score:
            best = neighbourhood
            highest_score = score

        # store information in table
        
        ### OLD
        #table.append([i, max_houses, score])
    
    # make a visualisation of the best random neighbourhood and save it as an image
    visualise(best, highest_score, "random_visualisation-"+ str(max_houses))

    for i in best:
        corner_1 = str(int(i.x0)) + "," + str(int(i.y0))
        corner_2 = str(int(i.y1)) + "," + str(int(i.y0))
        corner_3 = str(int(i.y1)) + "," + str(int(i.x1))
        corner_4 = str(int(i.x0)) + "," + str(int(i.x1))
        table.append([i.id, corner_1, corner_2, corner_3, corner_4, i.name])
    
    table.append(["networth", highest_score])

    # turn the table into a dataframe
    df_random = pd.DataFrame(table, columns=["structure", "corner_1", "corner_2", "corner_3", "corner_4", "type"]).set_index("structure")

    # save the dataframe as a csv file
    df_random.to_csv("results/output.csv")

    # make a plot of the algorithms performance
    #performanceplot("random", max_houses, "dist", df_random.score)
