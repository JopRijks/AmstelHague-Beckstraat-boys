import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as rect
import matplotlib.collections as coll
from classes.objects import Borders

def visualise(nb, score, x=None):
    ax = plt.axes()
    ax.set_xlim(0,Borders().maxX)
    ax.set_ylim(0,Borders().maxY)

    ax.set_facecolor("green")
    ax.set_title("random score: "+str(score))

    for i in range(len(nb)):
        if nb[i].name == "maison":
            # maison1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -6,nb[i].y0 -6), 24, 22)])
            # maison1.set_color("gray")
            # ax.add_collection(maison1)
            maison = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 12, 10)])
            maison.set_color("yellow")
            ax.add_collection(maison)
        
        if nb[i].name == "bungalow":
            # bungalow1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -3,nb[i].y0 -3), 17, 13)])
            # bungalow1.set_color("gray")
            # ax.add_collection(bungalow1)
            bungalow = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 11, 7)])
            bungalow.set_color("brown")
            ax.add_collection(bungalow)

        if nb[i].name == "sfh":
            # sfh1 = coll.PatchCollection([rect.Rectangle((nb[i].x0 -2,nb[i].y0 -2), 12, 12)])
            # sfh1.set_color("gray")
            # ax.add_collection(sfh1)            
            sfh = coll.PatchCollection([rect.Rectangle((nb[i].x0,nb[i].y0), 8, 8)])
            sfh.set_color("red")
            ax.add_collection(sfh)

        if nb[i].name == "WATER":
            waterLocation = rect.Rectangle((nb[i].x0, nb[i].y0), nb[i].width, nb[i].length)
            water = coll.PatchCollection([waterLocation])
            water.set_color("dodgerblue")
            ax.add_collection(water)
    
    if x != None:
        plt.savefig("results/"+str(x) + ".png")
    plt.close()

