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
                while(location_checker(house, neighbourhood) == False):
                    # print(i)
                    house = House("maison", i)
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)
            if location_checker(house, neighbourhood) == False:
                while(location_checker(house, neighbourhood) == False):
                    # print(i)
                    house = House("bungalow", i)
        elif i < amount_sfh:
            house = House("sfh",i)
            if location_checker(house, neighbourhood) == False:
                while(location_checker(house, neighbourhood) == False):
                    # print(i)
                    house = House("sfh", i)
        neighbourhood.append(house)
    print(neighbourhood, len(neighbourhood))


def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    vert = range(house.y0, house.y1)
    horz = range(house.x0, house.x1)
    for i in neighbourhood:
        if i.x0 in horz or i.x1 in horz:
            if i.y0 in vert or i.y1 in vert:
                # print(i.coordinates, house.coordinates)
                return False
        elif i.y0 in vert or i.y1 in vert:
            min_distance = min([float(house.x0-i.x1),float(house.x1-i.x0)])            
            if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                # print(min_distance)
                return False
            return True
        elif i.x0 in horz or i.x1 in horz:
            min_distance = min([float(house.y0-i.y1),float(house.y1-i.y0)])            
            if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                # print(min_distance)
                return False
            return True
        else:
            if house.y1 < i.y0:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)
                    if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        # print(min_distance)                        
                        return False 
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)
                    if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        # print(min_distance)
                        return False 
            elif house.y0 > i.y1:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                    if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        # print(min_distance)                    
                        return False 
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                    if house.free_area > abs(min_distance) and i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        # print(min_distance)
                        return False                            

    return True

def distanceCalc(x0,y0,x1,y1):
    return float(((x1-x0)**2+(y1-y0)**2)**0.5)

housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh)