"""
builder.py

Wordt gebruikt om een wijkindeling samen te stellen die aan de vereisten voldoet.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

# in dit bestand komt een algoritme
import pandas as pd

from code.classes.objects import Water, House
from code.helpers.visualize import visualise
from code.helpers.location import location_checker
from code.helpers.score import scorecalculator, distance_check

def waterbuilder(choice, neighbourhood):
    
    # collect all csv files and convert them to pandas dataframe and select the wanted file with the choice variable
    df = [pd.read_csv("data/wijk_1.csv"),pd.read_csv("data/wijk_2.csv"),pd.read_csv("data/wijk_3.csv")][choice]

    # loop through all dataframe rows
    for index, rows in df.iterrows(): 

    # Collect all the wanted data from the dataframe row
        ID = index
        name = rows.type
        x0 = int(rows.bottom_left_xy.split(',')[0])
        x1 = int(rows.top_right_xy.split(',')[0])
        y0 = int(rows.bottom_left_xy.split(',')[1])
        y1 = int(rows.top_right_xy.split(',')[1])
        width = abs(x0-x1)
        length = abs(y0-y1)

        # make from the collected values a water object and append it to the neighbourhood
        water = Water(ID,name, width, length, x0,x1,y0,y1)
        neighbourhood.append(water)

    # return the neighbourhood
    return neighbourhood

def housebuilder(max_houses,amount_maison,amount_bungalow,amount_sfh, neighbourhood):

    # loop for every house that has to be placed
    for i in range(max_houses):

        # check if the house type should be maison
        if i < amount_maison:
            # create house with random coorinates 
            house = House("maison", i)
            
            # if it violates any rule create a new house with random coorinates
            while location_checker(house, neighbourhood) == False:
                house = House("maison", i)

        # check if the house type should be bungalow
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)

            # if it violates any rule create a new house with random coorinates
            while location_checker(house, neighbourhood) == False:
                house = House("bungalow", i)

        # check if the house type should be single family house     
        else:
            house = House("sfh",i)

            # if it violates any rule create a new house with random coorinates
            while location_checker(house, neighbourhood) == False:
                house = House("sfh", i)

        # append house to neighbourhood and calculate the distance 
        neighbourhood.append(house)
        neighbourhood = distance_check(neighbourhood)
    score = scorecalculator(neighbourhood)
    return neighbourhood, score
