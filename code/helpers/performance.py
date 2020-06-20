"""
performance.py

creates a plot of the performance of an algorithm
"""

import matplotlib.pyplot as plt
import seaborn as sns

def performanceplot(algorithm, n, plottype, x, y=None):
    # make a plot of the algorithms performance
    sns.set(style="darkgrid")
    
    # create a histogram
    if plottype == "dist":
        ax = sns.distplot(x)
        ax.set_xlabel("Score (in Euros)")
        ax.set_ylabel("Iterations")
    
    # create a line diagram
    if plottype == "line":
        ax = sns.lineplot(x, y)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Score (in Euros)")

    ax.set_title("{} algorithm for {} houses".format(algorithm, n))

    # save plot as image
    ax.figure.savefig("results/"+plottype+"plot_"+algorithm+"-"+str(n)+".png")
