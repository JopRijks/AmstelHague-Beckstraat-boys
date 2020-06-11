class Water(object):
    
    def __init__(self, type, dimensie, verplichte_vrije_ruimte, extra_ruimte, waarde,
        prijs_verhoging_per_meter, ID):
        self.type = typeWater
        self.dimensie = (int(dimensie[0],
                                int(dimensie[1]))
        self.verplichte_vrije_ruimte = (verplichte_vrije_ruimte)
        self.extra_ruimte = extra_ruimte
        self.waarde = waarde
        self.prijs_verhoging_per_meter = prijs_verhoging_per_meter
        self.ID  = ID


class House(object):
    def __init__(self, typeHuis, dimensie, verplichte_vrije_ruimte, extra_ruimte, waarde,
    prijs_verhoging_per_meter, ID):
        self.type = typeHuis
        self.dimensie = (int(dimensie[0],
                                int(dimensie[1]))
        self.verplichte_vrije_ruimte = (verplichte_vrije_ruimte)
        self.extra_ruimte = extra_ruimte
        self.waarde = waarde
        self.prijs_verhoging_per_meter = prijs_verhoging_per_meter
        self.ID  = ID