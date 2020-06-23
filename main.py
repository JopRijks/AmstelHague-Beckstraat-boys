"""
main.py

Wordt gebruikt om een oplossing te vinden voor het Amstelhaege probleem.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import sys
import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import time
import datetime

from code.helpers.score import scorecalculator
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.helpers.output_generator import output
from code.algorithms.random import random_algorithm
from code.algorithms.hillclimber import hillclimber_algorithm
from code.algorithms.greedy import greedy_algorithm

if __name__ == "__main__":
    # set time from start algorithm 
    t1 = time.time()

    ##################### set variables through command line input
    # check if number of input arguments is correct
    if len(sys.argv) != 5:
        print("wrong input \n use: [approach] [iterations] [number of houses] [water map]")
        print("approach: random, hillcliber, greedy, bestrandom-hillcimber or greedy-hillclimber")
        print("iterations: just a positive number")
        print("number of houses: choose 20, 40 or 60")
        print("water map: choose 0, 1 or 2")
        exit()
    else:

        # algorithm of choice can be random or hill climber
        approach = sys.argv[1]

        # number of iterations to execute the algorithm
        iterations = int(sys.argv[2])

        # default 100 iterations if input is 0 or negative
        if iterations < 1:
            iterations = 100

        # number of houses to be placed
        n_houses = int(sys.argv[3])

        # default 20 houses if input is below 1 or over 60
        if ((n_houses != 20) and (n_houses != 40) and (n_houses != 60)):
            n_houses = 20

        # 0 for wijk_1, 1 for wijk_2, 2 for wijk_3
        water_layout = int(sys.argv[4])
        if water_layout == 3:
            water_layout = 2
        elif ((water_layout < 0) or (water_layout > 3)):
            water_layout = 0

    # get current timestamp
    dt = datetime.datetime.now()
    ts = dt.strftime("%Y-%m-%d_%Hh%Mm%Ss")

    # execute hill climber algorithm
    if approach == "hillclimber":
        neighbourhood, score = hillclimber_algorithm(iterations, water_layout, n_houses)

    # execute greedy algorithm
    elif approach == "greedy":
        neighbourhood, score = greedy_algorithm(iterations, water_layout, n_houses)

    # execute greed-hillclimber algorithm
    elif approach == "hillclimber-greedy":
        neighbourhood, score = greedy_algorithm(iterations, water_layout, n_houses)
        neighbourhood, score = hillclimber_algorithm(iterations, water_layout, n_houses, neighbourhood, score, "greedy")

    elif approach == "bestrandom-hillclimber":
        neighbourhood, score = random_algorithm(iterations, water_layout, n_houses, ts)
        neighbourhood, score = hillclimber_algorithm(iterations, water_layout, n_houses, neighbourhood, score, "random")
    # if no algorithm or random is specified execute random algorithm
    else:
        neighbourhood, score = random_algorithm(iterations, water_layout, n_houses, ts)

    # generate output and print dataframe
    output(neighbourhood, score, approach, iterations, n_houses, water_layout, ts)
    print(output)
    
    # set time from end algorithm and print the total duration
    t2 = time.time()
    print("Duration of algorithm: {} seconds".format(t2-t1))