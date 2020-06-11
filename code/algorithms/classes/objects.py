# door middel van object-oriented programming worden in dit bestand classes vastgesteld
import random as rd

#borders
maxX = 180
maxY = 160
class Water:
    """Initializes water"""
    def __init__(self, grid, width, length, x0, x1, y0, y1):
        self.width = width
        self.length = length
        self.id = grid
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

class House:
    def __init__(self, type, house_number, x=None, y=None):
        self.id = house_number
        if type == "sfh":
            self.name = "sfh"
            self.length = 8
            self.width = 8
            self.price = 285000
            self.free_area = 2
            self.price_increasement = float(0.03)

        if type == "bungalow":
            self.name = "bungalow"
            self.length = 7
            self.width = 11
            self.price = 399000
            self.free_area = 3
            self.price_increasement = float(0.04)

        if type == "maison":
            self.name = "maison"
            self.length = 10
            self.width = 12
            self.price = 610000
            self.free_area = 6
            self.price_increasement = float(0.06)

        if x==None or y==None:
            x = rd.randrange(self.free_area, (maxX - self.free_area - self.length))
            y = rd.randrange(self.free_area, (maxY - self.free_area - self.width))

        self.x0 = x
        self.x1 = x + self.width
        self.y0 = y
        self.y1 = y + self.length
        self.coordinates = (x,y)