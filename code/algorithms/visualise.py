import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as rect
import matplotlib.collections as coll
from functions import housebuilder, waterbuilder

def visualise(neighbourhood, score, x=None):
    ax = plt.axes()
    ax.set_xlim(0,160)
    ax.set_ylim(0,180)

    ax.set_facecolor("green")
    ax.set_title("random score: "+str(score))

    for i in range(len(neighbourhood)):
        if neighbourhood[i].name == "maison":
            # maison1 = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0 -6,neighbourhood[i].y0 -6), 24, 22)])
            # maison1.set_color("gray")
            # ax.add_collection(maison1)
            maison = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0,neighbourhood[i].y0), 12, 10)])
            maison.set_color("yellow")
            ax.add_collection(maison)
        
        if neighbourhood[i].name == "bungalow":
            # bungalow1 = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0 -3,neighbourhood[i].y0 -3), 17, 13)])
            # bungalow1.set_color("gray")
            # ax.add_collection(bungalow1)
            bungalow = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0,neighbourhood[i].y0), 11, 7)])
            bungalow.set_color("brown")
            ax.add_collection(bungalow)

        if neighbourhood[i].name == "sfh":
            # sfh1 = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0 -2,neighbourhood[i].y0 -2), 12, 12)])
            # sfh1.set_color("gray")
            # ax.add_collection(sfh1)            
            sfh = coll.PatchCollection([rect.Rectangle((neighbourhood[i].x0,neighbourhood[i].y0), 8, 8)])
            sfh.set_color("red")
            ax.add_collection(sfh)

        if neighbourhood[i].name == "WATER":
            waterLocation = rect.Rectangle((neighbourhood[i].x0, neighbourhood[i].y0), neighbourhood[i].width, neighbourhood[i].length)
            water = coll.PatchCollection([waterLocation])
            water.set_color("dodgerblue")
            ax.add_collection(water)
    
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
    neighbourhood = []
    choice = 0 #0 1 of 2 voor water wijk
    neighbourhood = waterbuilder(choice, neighbourhood)
    neighbourhood, score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)
    visualise(neighbourhood, score, "test"+str(i))