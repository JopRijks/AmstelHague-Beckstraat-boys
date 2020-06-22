"""
location.py

Wordt gebruikt om de vrijstand van een huis te berekenen en om 
te controleren of de locatie van een huis aan de vereisten voldoet.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    mindistance= []
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
            if (house.x0 -1 <= i.x0 and house.x1+1 >= i.x0) or (house.x0-1 <= i.x1 and house.x1+1 >= i.x1):
                if (house.y0-1 <= i.y0 and house.y1+1 >= i.y0) or (house.y0-1 <= i.y1 and house.y1+1 >= i.y1):
                    return False
            if (house.y0-1 <= i.y0 and house.y1+1 >= i.y0) or (house.y0-1 <= i.y1 and house.y1+1 >= i.y1):
                min_distance = min([abs(house.x0-i.x1),abs(house.x1-i.x0),abs(house.x1-i.x1),abs(house.x0-i.x0)])   
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
            elif (house.x0 -1 <= i.x0 and house.x1+1 >= i.x0) or (house.x0-1 <= i.x1 and house.x1+1 >= i.x1):
                min_distance = min([abs(house.y0-i.y1),abs(house.y1-i.y0),abs(house.y1-i.y1),abs(house.y0-i.y0)])         
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
            elif house.y1 < i.y0:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False                                           
            elif house.y0 > i.y1:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden                    
                        return False
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
    return True

def distanceCalc(x0,y0,x1,y1):
    return abs(((x1-x0)**2+(y1-y0)**2)**0.5)