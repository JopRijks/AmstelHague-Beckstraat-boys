import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as rect
import matplotlib.collections as coll
from functions import housebuilder

def visualise(houses, x=None):

    ax = plt.axes()
    ax.set_xlim(0,180)
    ax.set_ylim(0,160)

    ax.set_facecolor("green")

    for i in range(len(houses)):
        if houses[i].name == "maison":
            maison = coll.PatchCollection([rect.Rectangle((houses[i].x0,houses[i].y0), 12, 10)])
            maison.set_color("yellow")
            ax.add_collection(maison)
        
        if houses[i].name == "bungalow":
            bungalow = coll.PatchCollection([rect.Rectangle((houses[i].x0,houses[i].y0), 11, 7)])
            bungalow.set_color("brown")
            ax.add_collection(bungalow)

        if houses[i].name == "sfh":
            sfh = coll.PatchCollection([rect.Rectangle((houses[i].x0,houses[i].y0), 8, 8)])
            sfh.set_color("red")
            ax.add_collection(sfh)

    if x != None:
        plt.savefig(str(x) + ".png")
    plt.close()

max_houses = 20
fraction_sfh = 0.6
fraction_bungalow = 0.25 
fraction_maison = 0.15
amount_sfh = max_houses * fraction_sfh
amount_bungalow = max_houses * fraction_bungalow
amount_maison = max_houses * fraction_maison

for i in range(10):
    neighbourhood = housebuilder(max_houses,amount_maison,amount_bungalow,amount_sfh)
    visualise(neighbourhood, "test"+str(i))