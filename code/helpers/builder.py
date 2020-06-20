# in dit bestand komt een algoritme
import pandas as pd

from code.classes.objects import Water, House
from code.helpers.visualize import visualise
from code.helpers.location import location_checker
from code.helpers.score import scorecalculator, distance_check

def waterbuilder(choice, neighbourhood):
    df = [pd.read_csv("data/wijk_1.csv"),pd.read_csv("data/wijk_2.csv"),pd.read_csv("data/wijk_3.csv")][choice]
    for index, rows in df.iterrows(): 
    # Create list for the current row 
        ID = index
        name = rows.type
        x0 = int(rows.bottom_left_xy.split(',')[0])
        x1 = int(rows.top_right_xy.split(',')[0])
        y0 = int(rows.bottom_left_xy.split(',')[1])
        y1 = int(rows.top_right_xy.split(',')[1])
        width = abs(x0-x1)
        length = abs(y0-y1)
        water = Water(ID,name, width, length, x0,x1,y0,y1)
        neighbourhood.append(water)
    return neighbourhood

def housebuilder(max_houses,amount_maison,amount_bungalow,amount_sfh, neighbourhood):
    for i in range(max_houses):
        if i < amount_maison:
            house = House("maison", i)
            if location_checker(house, neighbourhood) == False:
                while location_checker(house, neighbourhood) == False:
                    house = House("maison", i)
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)
            if location_checker(house, neighbourhood) == False:
                while location_checker(house, neighbourhood) == False:
                    house = House("bungalow", i)
        else:
            house = House("sfh",i)
            if location_checker(house, neighbourhood) == False:
                while location_checker(house, neighbourhood) == False:
                    house = House("sfh", i)
        neighbourhood.append(house)
        neighbourhood = distance_check(neighbourhood)
    score = scorecalculator(neighbourhood)
    return neighbourhood, score
