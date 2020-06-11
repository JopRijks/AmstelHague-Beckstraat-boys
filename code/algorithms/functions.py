# in dit bestand komt een algoritme
from classes.grid import *
from classes.objects import *
import random as rd
import numpy as np

max_houses = 20
fraction_sfh = 0.6
fraction_bungalow = 0.25 
fraction_maison = 0.15
amount_sfh = max_houses * fraction_sfh
amount_bungalow = max_houses * fraction_bungalow
amount_maison = max_houses * fraction_maison


def housebuilder(max_houses,amount_maison,amount_bungalow,amount_sfh):
    neighbourhood = []
    for i in range(max_houses):
        if i < amount_maison:
            house = House("maison", i)
            if location_checker(house, neighbourhood) == False:
                print("ALARM ALARM ALARM")
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)
            if location_checker(house, neighbourhood) == False:
                print("ALARM ALARM ALARM")
        elif i < max_houses:
            house = House("sfh",i)
            if location_checker(house, neighbourhood) == False:
                print("ALARM ALARM ALARM")
        neighbourhood.append(house)
    print(neighbourhood, len(neighbourhood))


def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    vert = range(house.y0, house.y1)
    horz = range(house.x0, house.x1)
    for i in neighbourhood:
        if i.x0 in horz or i.x1 in horz and i.y0 in vert or i.y1 in vert:
            return False
        elif i.y0 in vert or i.y1 in vert:
            min_distance = min([float(house.x0-i.x1),float(house.x1-i.x0)])            
            if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                return False
            return True
        elif i.x0 in horz or i.x1 in horz:
            min_distance = min([float(house.y0-i.y1),float(house.y1-i.y0)])            
            if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                return False
            return True
        else:
            


    # diagonal check
    # for i in neighbourhood:
    #     for j in [house.x0,house.x1]:
    #         for k in [house.y0,house.y1]:
    #             for l in [i.x0,i.x1]:
    #                 for m in [i.y0,i.y1]:
    #                     distances.append(calculateDistance(j,k,l,m))
    # return True
    # test = [i for i in distances if i < 2]
    # if len(test) > 0:
    #     print(test)
    #     return False
    # else:
    #     return True
    return True
housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh)