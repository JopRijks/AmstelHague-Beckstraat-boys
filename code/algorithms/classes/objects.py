# door middel van object-oriented programming worden in dit bestand classes vastgesteld

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
    def __init__(self, type, x, y):
        if type == "sfh":
            self.name = "sfh"
            self.length = 8
            self.width = 8
            self.price = 285000
            self.free_area = 2
            self.price_increasement = float(0.03)

        if type == "bungalow":
            self.name = "bungalow"
            self.length = 11
            self.width = 7
            self.price = 399000
            self.free_area = 3
            self.price_increasement = float(0.04)

        if type == "maison":
            self.name = "maison"
            self.length = 12
            self.width = 10
            self.price = 610000
            self.free_area = 6
            self.price_increasement = float(0.06)

    	self.x0 = x
        self.x1 = x +self.width
        self.y0 = y
        self.y1 = y +self.length