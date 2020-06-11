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
        