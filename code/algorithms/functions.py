# in dit bestand komt een algoritme
from classes.grid import *
from classes.objects import *
import random as rd
import numpy as np
import pandas as pd

max_houses = 20
fraction_sfh = 0.6
fraction_bungalow = 0.25 
fraction_maison = 0.15
amount_sfh = max_houses * fraction_sfh
amount_bungalow = max_houses * fraction_bungalow
amount_maison = max_houses * fraction_maison

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
                for k in range(1000):
                    house = House("maison", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        elif i < amount_bungalow + amount_maison:
            house= House("bungalow",i)
            if location_checker(house, neighbourhood) == False:
                for k in range(1000):
                    house = House("bungalow", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        else:
            house = House("sfh",i)
            if location_checker(house, neighbourhood) == False:
                for k in range(1000):
                    house = House("sfh", i)
                    if location_checker(house, neighbourhood) == True:
                        break
        neighbourhood.append(house)
    score = scorecalculator(neighbourhood)
    return neighbourhood, score

def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    mindistance= []
    vert = list(range(house.y0, house.y1))
    horz = list(range(house.x0, house.x1))
    for i in neighbourhood:
        if i.name == "WATER":
            horzWater = list(range(i.x0, i.x1))
            vertWater = list(range(i.y0, i.y1))
            if (house.x0 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x0 in horzWater and house.y1 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y1 in vertWater):
                return False     
        else:
            if (house.x0 -2 <= i.x0 and house.x1+2 >= i.x0) or (house.x0-2 <= i.x1 and house.x1+2 >= i.x1):
                if (house.y0-2 <= i.y0 and house.y1+2 >= i.y0) or (house.y0-2 <= i.y1 and house.y1+2 >= i.y1):
                    return False
            if i.y0 in vert or i.y1 in vert:
                min_distance = min([abs(house.x0-i.x1),abs(house.x1-i.x0),abs(house.x1-i.x1),abs(house.x0-i.x0)])
                mindistance.append(min_distance)          
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
                elif min_distance < i.shortest_distance :
                    #print(i.shortest_distance,min_distance)
                    i.shortest_distance = min_distance
            elif i.x0 in horz or i.x1 in horz:
                min_distance = min([abs(house.y0-i.y1),abs(house.y1-i.y0),abs(house.y1-i.y1),abs(house.y0-i.y0)])
                mindistance.append(min_distance)           
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
                elif min_distance < i.shortest_distance :
                    #print(i.shortest_distance,min_distance)
                    i.shortest_distance = min_distance
            elif house.y1 < i.y0:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance                                                    
            elif house.y0 > i.y1:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden                    
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance 
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance
    if len(mindistance) > 0:
        #print(min(mindistance))
        house.shortest_distance = min(mindistance)
    return True

def distanceCalc(x0,y0,x1,y1):
    return abs(((x1-x0)**2+(y1-y0)**2)**0.5)

def scorecalculator(neighbourhood):
    score = 0
    for house in neighbourhood:
        if house.name != "WATER":
            score = score + (house.shortest_distance - house.free_area)*house.price_increasement
    return score

neighbourhood = []
choice = 0 #0 1 of 2 voor water wijk
neighbourhood = waterbuilder(choice, neighbourhood)
neighbourhood, score = housebuilder(max_houses, amount_maison,amount_bungalow,amount_sfh, neighbourhood)