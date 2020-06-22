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
    # set axis 
    ax = plt.axes()
    ax.set_xlim(0,Borders().maxX)
    ax.set_ylim(0,Borders().maxY)

    # set background color
    ax.set_facecolor("lightgreen")

    # title of the plot is the score in correct currency formatting
    title = "Score: €{:,.2f}".format(score)
    score_main, score_fractional = title.split(".")[0], title.split(".")[1]
    new_score_main = score_main.replace(",", ".")
    title = new_score_main + "," + score_fractional
    ax.set_title(title)

    # check if object is water or a kind of house and every kind of object gets another colour and size assigned and is placed in a grid
    for i in range(len(nb)):
        if nb[i].name == "WATER":
            waterLocation = rect.Rectangle((nb[i].x0, nb[i].y0), nb[i].width, nb[i].length)
            water = coll.PatchCollection([waterLocation])
            water.set_color("lightskyblue")
            ax.add_collection(water)
    
        elif nb[i].type == "maison":
            maison = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 12, 10)])
            maison.set_color("plum")
            ax.add_collection(maison)
        
        elif nb[i].type == "bungalow":
            bungalow = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 11, 7)])
            bungalow.set_color("burlywood")
            ax.add_collection(bungalow)

        elif nb[i].type == "sfh":          
            sfh = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 8, 8)])
            sfh.set_color("indianred")
            ax.add_collection(sfh)

    # save the file in the results folder and close it
    plt.savefig("results/" + str(x) + ".png")
    plt.close()
