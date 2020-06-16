import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "helpers"))

import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt

from code.helpers.score import scorecalculator
from code.helpers.visualize import visualise
from code.helpers.builder import waterbuilder, housebuilder
from code.algorithms.random import random_algorithm

if __name__ == "__main__":

    # set variables through input
    max_houses = int(sys.argv[1])
    iterations = int(sys.argv[2])
    water_layout = int(sys.argv[3])
    
    random_algorithm(iterations, water_layout, max_houses)