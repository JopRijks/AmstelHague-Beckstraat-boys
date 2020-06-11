class Water(object):
    def __init__(self, index, x1, x2, y1, y2, width, length):
        self.id = index
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = width
        self.length = length

class House:
    def __init__(self, type, id, x=None, y=None):
        if type == "single family home":
            self.name = "Eensgezinswoning"
            self.length = 8
            self.width = 8
            self.price = 285000
            self.verplichte_vrijstand = 2
            self.verbetering = float(0.03)

        if kind == "Bungalow":
            self.name = "B"
            self.length = 20
            self.width = 15
            self.price = 399000
            self.verplichte_vrijstand = 6
            self.verbetering = 0.02
        # Maison
        if kind == "M":
            self.name = "M"
            self.length = 22
            self.width = 21
            self.price = 610000
            self.verplichte_vrijstand = 12
            self.verbetering = 0.03
        
        if x==None:
            x = randint(self.verplichte_vrijstand, (X_MAX - self.verplichte_vrijstand - self.length))
        if y==None:
            y = randint(self.verplichte_vrijstand, (Y_MAX - self.verplichte_vrijstand - self.width))

        # each house gets a unique id and coordinates of left upper corner
        self.id = id
        self.coordinates = (x, y)
        self.shortest_distance = None
        self.x1 = x
        self.x2 = x + self.length
        self.y1 = y
        self.y2 = y + self.width