"""
performance.py

Wordt gebruikt om een diagram te plotten van de prestaties van een algoritme.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

import matplotlib.pyplot as plt
import seaborn as sns
import time

def performanceplot(algorithm, iterations, n, ts, x, y=None):
    plt.figure()
    # make a plot of the algorithms performance
    sns.set(style="darkgrid")
    
    # plot for random algorithm
    if algorithm == "Random":
        ax = sns.distplot(x)
        ax.set_xlabel("Score (€)")
        ax.set_ylabel("Iterations")
    
    # plot for hill climber algorithm with random start
    if algorithm == "Hillclimber-random":
        ax = sns.lineplot(x, y)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Score (€)")

    # plot for hill climber algorithm with best random start
    if algorithm == "Hillclimber-bestrandom":
        ax = sns.lineplot(x, y)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Score (€)")

    # plot for hill climber algorithm with greedy start
    if algorithm == "Hillclimber-greedy":
        ax = sns.lineplot(x, y)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Score (€)")

    # plot for greedy algorithm
    if algorithm == "Greedy":
        ax = sns.lineplot(x, y)
        ax.set_xlabel("Number of houses placed")
        ax.set_ylabel("Total score (€)")

    # create title
    ax.set_title("{} algorithm for {} houses".format(algorithm, n))

    # save plot as image
    ax.figure.savefig("results/plot.png")
    ax.figure.savefig("results/plots/"+str(ts)+"-plot-"+algorithm+"-"+str(iterations)+"-"+str(n)+".png")

    sns.set()
    plt.close()
