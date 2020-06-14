import pandas as pd
import random as rd
import numpy as np
import math
import matplotlib.pyplot as plt

from helpers.score import scorecalculator
from helpers.visualize import visualise
from helpers.builder import waterbuilder, housebuilder

if __name__ == "__main__":
    max_houses = 20
    iterations = 100
    
    water_layout = 0 #0 1 of 2 voor water wijk
    
    fraction_sfh,fraction_bungalow,fraction_maison = 0.6, 0.25, 0.15
    amount_sfh, amount_bungalow, amount_maison = max_houses * fraction_sfh, max_houses * fraction_bungalow, max_houses * fraction_maison
    
    highest_score, best, table = 0, 0, []
    
    for i in range(iterations):
        neighbourhood = []
        neighbourhood = waterbuilder(water_layout, neighbourhood)
        neighbourhood, score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)
        table.append([i, max_houses, score])
        if score > highest_score:
            best = neighbourhood
            highest_score = score
    df = pd.DataFrame(table, columns = ["iteration", "max_houses","score"]).set_index("iteration")
    df.to_csv("results/"+ str(iterations)+"-random.csv")
    
    df.hist(column = "score")
    plt.savefig("results/distribution_random.png")
    plt.close()
    visualise(best, highest_score, "bestrandom")