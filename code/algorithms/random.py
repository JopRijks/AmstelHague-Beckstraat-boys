"""
random.py
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt

from helpers.score import scorecalculator
from helpers.visualize import visualise
from helpers.builder import waterbuilder, housebuilder

def random_algorithm(iterations, water_layout, max_houses):
    # standard neighbourhood distributiion of the houses
    fraction_sfh,fraction_bungalow,fraction_maison = 0.6, 0.25, 0.15
    amount_sfh, amount_bungalow, amount_maison = max_houses * fraction_sfh, max_houses * fraction_bungalow, max_houses * fraction_maison

    highest_score, best, table = 0, 0, []
    # iterate through different creations of the neighbourhood
    for i in range(iterations):
        # create neighbourhood, place water and build houses, collect neighbourhood and score
        neighbourhood = []
        neighbourhood = waterbuilder(water_layout, neighbourhood)
        neighbourhood, score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)
        
        # add iteration number, max_houses and score to the table
        table.append([i, max_houses, score])
        
        # if the score of the neighbourhood in this iteration is the highest till now than save the neighbourhood and the score
        if score > highest_score:
            best = neighbourhood
            highest_score = score
    
    # save the information from the iteration
    df_random = pd.DataFrame(table, columns = ["iteration", "max_houses","score"]).set_index("iteration")
    df_random.to_csv("results/"+ str(iterations)+"-"+str(max_houses)+"-random.csv")
    
    # make a histogram of the scores from all the neighbourhoods made through the iterations
    df_random.hist(column = "score")
    plt.savefig("results/distribution_random.png")
    plt.close()
    
    # make a visualisation of the best random neighbourhood and save it
    visualise(best, highest_score, "bestrandom")