import sys
import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt
import time

from code.helpers.score import scorecalculator
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.algorithms.random import random_algorithm
from code.algorithms.hillclimber import hillclimber_algorithm
from code.algorithms.greedy import greedy_algorithm

if __name__ == "__main__":

    ##################### set variables through command line input
    t1 = time.time()
    # check if number of input arguments is correct
    if len(sys.argv) != 5:
        print("wrong input \n use: [approach] [iterations] [number of houses] [water map]")
        print("approach: random, hillcliber or greedy")
        print("iterations: just a positive number")
        print("number of houses: choose 20, 40 or 60")
        print("water map: choose 0, 1 or 2")
        exit()
        # approach = "random"
        # iterations = 100
        # n_houses = 20
        # water_layout = 0

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
        if n_houses < 1:
            n_houses = 20
        if n_houses > 80:
            n_houses = 20

        # 0 for wijk_1, 1 for wijk_2 or 2 for wijk_3
        water_layout = int(sys.argv[4])
        if water_layout < 0:
            water_layout = 0
        if water_layout > 2:
            water_layout = 0

    # execute hill climber algorithm
    if approach == "hillclimber":
        hillclimber_algorithm(iterations, water_layout, n_houses)

    # execute greedy algorithm
    elif approach == "greedy":
       greedy_algorithm(iterations, water_layout, n_houses)

    #if no algorithm is specified execute random algorithm
    else:
        random_algorithm(iterations, water_layout, n_houses)
    
    t2 = time.time()
    print(t2-t1)