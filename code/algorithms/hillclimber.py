"""
hill climber
"""

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt

from code.helpers.score import scorecalculator
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder

def hillclimber_algorithm(iterations, water_layout, max_houses):

    ################################ start by creating a random neighbourhood ###################
    
    # standard neighbourhood distribution of the houses
    amount_sfh, amount_bungalow, amount_maison = max_houses*0.6, max_houses*0.25, max_houses*0.15

    # create neighbourhood, place water and build houses, collect neighbourhood and score
    neighbourhood = []
    neighbourhood = waterbuilder(water_layout, neighbourhood)
    neighbourhood, score = housebuilder(max_houses, amount_maison, amount_bungalow, amount_sfh, neighbourhood)
    
    ################################ now iterate using the hill climber method ####################


    # make a visualisation of the best score and save it
    visualise(neighbourhood, score, "hillclimber")
