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
            # maison1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -6,nb[i].y0 -6), 24, 22)])
            # maison1.set_color("gray")
            # ax.add_collection(maison1)
            maison = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 12, 10)])
            maison.set_color("plum")
            ax.add_collection(maison)
        
        if nb[i].name == "bungalow":
            # bungalow1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -3,nb[i].y0 -3), 17, 13)])
            # bungalow1.set_color("gray")
            # ax.add_collection(bungalow1)
            bungalow = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 11, 7)])
            bungalow.set_color("burlywood")
            ax.add_collection(bungalow)

        if nb[i].name == "sfh":
            # sfh1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -2,nb[i].y0 -2), 12, 12)])
            # sfh1.set_color("gray")
            # ax.add_collection(sfh1)            
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
