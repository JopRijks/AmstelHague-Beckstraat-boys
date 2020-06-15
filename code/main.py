import sys
import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt

from helpers.score import scorecalculator
from helpers.visualize import visualise
from helpers.builder import waterbuilder, housebuilder
from algorithms.random import random_algorithm


if __name__ == "__main__":
    # set variables through input
    max_houses = int(sys.argv[1])
    iterations = int(sys.argv[2])
    water_layout = int(sys.argv[3])
    
    random_algorithm(iterations, water_layout, max_houses)
    
    


