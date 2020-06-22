"""
location.py

Wordt gebruikt om de vrijstand van een huis te berekenen en om 
te controleren of de locatie van een huis aan de vereisten voldoet.

Programmeertheorie
Universiteit van Amsterdam

Jop Rijksbaron, Robin Spiers & Vincent Kleiman
"""

def location_checker(house, neighbourhood):
    # loop through the neighbourhood
    for i in neighbourhood:

        # check if i is water, if i is water than the only regulation is that the house can't stand on water
        if i.name == "WATER":

            # collect x and y ranges of water
            horzWater = list(range(i.x0, i.x1))
            vertWater = list(range(i.y0, i.y1))

            # check if one corner of the house is placed on water
            if (house.x0 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x0 in horzWater and house.y1 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y1 in vertWater):
                return False     
        else:
            # check if house is standing on another house, if yes return false
            if (house.x0 -1 <= i.x0 and house.x1+1 >= i.x0) or (house.x0-1 <= i.x1 and house.x1+1 >= i.x1):
                if (house.y0-1 <= i.y0 and house.y1+1 >= i.y0) or (house.y0-1 <= i.y1 and house.y1+1 >= i.y1):
                    return False

            # location if house is placed right or left from i
            if (house.y0-1 <= i.y0 and house.y1+1 >= i.y0) or (house.y0-1 <= i.y1 and house.y1+1 >= i.y1):

                # collect all possible distances if walls are next to eachother on x-axis, absoulte values because distances can't be negative
                min_distance = min([abs(house.x0-i.x1),abs(house.x1-i.x0),abs(house.x1-i.x1),abs(house.x0-i.x0)])

                # check if this distance is smaller than the obligated free space, if no then return false   
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): 
                    return False
                    
            # location if house is placed above or down from i
            elif (house.x0 -1 <= i.x0 and house.x1+1 >= i.x0) or (house.x0-1 <= i.x1 and house.x1+1 >= i.x1):

                # collect all possible distances if walls are next to eachother on x-axis, absoulte values because distances can't be negative
                min_distance = min([abs(house.y0-i.y1),abs(house.y1-i.y0),abs(house.y1-i.y1),abs(house.y0-i.y0)])

                # check if this distance is smaller than the obligated free space, if no then return false         
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): 
                    return False

            # diagonal distance check         
            elif house.y1 < i.y0:

                # location check if house is down left
                if house.x1 < i.x0:

                    # calculate euclidean distance
                    min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)

                    # check if this distance is smaller than the obligated free space, if no then return false    
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): 
                        return False

                # location check if house is down right
                elif house.x0 > i.x1:

                    # calculate euclidean distance
                    min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)

                    # check if this distance is smaller than the obligated free space, if no then return false    
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): 
                        return False                                           
            
            elif house.y0 > i.y1:

                # location check if house is upper left
                if house.x1 < i.x0:

                    # calculate euclidean distance
                    min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance):                     
                        return False

                # location check if house is upper right         
                elif house.x0 > i.x1:

                    # calculate euclidean distance
                    min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): 
                        return False
    return True

def distanceCalc(x0,y0,x1,y1):
    
    # calculate euclidian distance
    return abs(((x1-x0)**2+(y1-y0)**2)**0.5)