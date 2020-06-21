"""
visualize.py

Wordt gebruikt om de kaart van de samengestelde wijk te visualiseren.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as rect
import matplotlib.collections as coll

from code.classes.objects import Borders

def visualise(nb, score, x=None):
    ax = plt.axes()

    ax.set_xlim(0,Borders().maxX)
    ax.set_ylim(0,Borders().maxY)

    ax.set_facecolor("lightgreen")

    # title of the plot is the score in correct currency formatting
    title = "Score: €{:,.2f}".format(score)
    score_main, score_fractional = title.split(".")[0], title.split(".")[1]
    new_score_main = score_main.replace(",", ".")
    title = new_score_main + "," + score_fractional
    ax.set_title(title)

    for i in range(len(nb)):
        if nb[i].name == "maison":
            maison = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 12, 10)])
            maison.set_color("plum")
            ax.add_collection(maison)
        
        if nb[i].name == "bungalow":
            bungalow = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 11, 7)])
            bungalow.set_color("burlywood")
            ax.add_collection(bungalow)

        if nb[i].name == "sfh":          
            sfh = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 8, 8)])
            sfh.set_color("indianred")
            ax.add_collection(sfh)

        if nb[i].name == "WATER":
            waterLocation = rect.Rectangle((nb[i].x0, nb[i].y0), nb[i].width, nb[i].length)
            water = coll.PatchCollection([waterLocation])
            water.set_color("lightskyblue")
            ax.add_collection(water)
    
    if x != None:
        plt.savefig("results/" + str(x) + ".png")
    plt.close()
