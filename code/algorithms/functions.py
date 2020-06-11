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


def housebuilder(amount_maison,amount_bungalow,amount_sfh):
    for i in range(int(amount_maison)):
        print(House("maison"))
    for i in range(int(amount_bungalow)):
        print(House("bungalow"))
    for i in range(int(amount_sfh)):
        print(House("sfh"))

housebuilder(amount_maison,amount_bungalow,amount_sfh)