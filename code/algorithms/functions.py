# in dit bestand komt een algoritme
from classes.types import *
from classes.modellen import *
import random as rd

def randomizer():
    print(test)

def GridSetUp():
    x_lengte = 160
    y_lengte = 160
    max_aantal_huizen = 20
    area = []

    area.append(Water(**water))

    # Create new houses based on the grid requirements
    for maison in range(gridInformation.totalAmountMaisons):
        residentialArea.append(House(**maison))

    for bungalow in range(gridInformation.totalAmountBungalows):
        residentialArea.append(House(**bungalow))

    for eengezinswoning in range(gridInformation.totalAmountEengezinswoningen):
        residentialArea.append(House(**eengezinswoning))

    # Initialize numpy grid (verticalY, horizontalX)
    numpyGrid = np.zeros((gridYLength,gridXLength), dtype="object")

    return area, numpyGrid, maxHouses