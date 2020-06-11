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
                for k in range(1000):
                    print(i)
                    house = House("maison", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)
            if location_checker(house, neighbourhood) == False:
                for k in range(1000):
                    print(i)
                    house = House("bungalow", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        else:
            house = House("sfh",i)
            if location_checker(house, neighbourhood) == False:
                for k in range(1000):
                    print(i)
                    house = House("sfh", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        neighbourhood.append(house)
    print([i.coordinates for i in neighbourhood], len(neighbourhood))
    return neighbourhood



def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    vert = range(house.y0, house.y1)
    horz = range(house.x0, house.x1)
    for i in neighbourhood:
        if (house.x0 -2 <= i.x0 and house.x1+2 >= i.x0) or (house.x0-2 <= i.x1 and house.x1+2 >= i.x1):
            if (house.y0-2 <= i.y0 and house.y1+2 >= i.y0) or (house.y0-2 <= i.y1 and house.y1+2 >= i.y1):
                print("test")
                return False
        if i.y0 in vert or i.y1 in vert:
            min_distance = min([float(house.x0-i.x1),float(house.x1-i.x0),float(house.x1-i.x1),float(house.x0-i.x0)])            
            if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                print(min_distance, i.free_area, house.free_area)
                return False
        if i.x0 in horz or i.x1 in horz:
            min_distance = min([float(house.y0-i.y1),float(house.y1-i.y0),float(house.y1-i.y1),float(house.y0-i.y0)])            
            if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                print(min_distance, i.free_area, house.free_area)
                return False
        if house.y1 < i.y0:
            if house.x1 < i.x0:
                min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    print(min_distance, i.free_area, house.free_area)                        
                    return False 
            elif house.x0 > i.x1:
                min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    print(min_distance, i.free_area, house.free_area)
                    return False 
        elif house.y0 > i.y1:
            if house.x1 < i.x0:
                min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    print(min_distance, i.free_area, house.free_area)                    
                    return False 
            elif house.x0 > i.x1:
                min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    print(min_distance, i.free_area, house.free_area)
                    return False
    return True

def distanceCalc(x0,y0,x1,y1):
    return float(((x1-x0)**2+(y1-y0)**2)**0.5)

housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh)