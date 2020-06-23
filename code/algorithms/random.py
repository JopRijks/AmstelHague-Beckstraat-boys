"""
random.py

Wordt voor het random algoritme gebruikt om tot een willekeurige oplossing te komen.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import pandas as pd
import matplotlib.pyplot as plt
from copy import deepcopy

from code.helpers.score import scorecalculator, distance_check
from code.helpers.visualize import create_map
from code.helpers.builder import waterbuilder, housebuilder
from code.helpers.performance import performanceplot

def random_algorithm(iterations, water_layout, max_houses, ts):
    """Peforming the random algorithm the desired iterations with the wanted water-layout and amount of houses""" 

    # standard neighbourhood distribution of the houses
    fraction_sfh,fraction_bungalow,fraction_maison = 0.6, 0.25, 0.15
    amount_sfh, amount_bungalow, amount_maison = max_houses * fraction_sfh, max_houses * fraction_bungalow, max_houses * fraction_maison

    highest_score, table = 0, []
    
    # performe the algorithm for a number of iterations
    for i in range(iterations):
        
        # create neighbourhood, place water and build houses, collect neighbourhood and score
        neighbourhood = []
        neighbourhood = waterbuilder(water_layout, neighbourhood)
        neighbourhood, new_score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)

        # if the score of the neighbourhood in this iteration is the highest till now than save the neighbourhood and the score
        if new_score > highest_score:
            best_map = deepcopy(neighbourhood)
            highest_score = deepcopy(new_score)

        # store iteration score in table
        table.append([i, new_score])
    
    # create dataframe to measure algorithm performance
    df_random = pd.DataFrame(table, columns = ["iteration", "score"])

    # make a visualisation of the best random neighbourhood and save it as an image
    create_map(best_map, highest_score, "Random", ts, "random_map-"+ str(max_houses))

    # make a plot of the algorithms performance
    performanceplot("Random", iterations, max_houses, ts, df_random.score)

    return best_map, highest_score
