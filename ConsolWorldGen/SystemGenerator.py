import random
from pathlib import Path
import sys
sys.path.append('../Traveller Programs')
import PlanetGenerator as pg

class System:
    gasGiant = False
    planet = None
    coords = ""
    def __init__(self, density, coords):
        r = random.randint(1,6)
        self.coords = coords
        if density == 0: r -= 2
        elif density == 1: r -= 1
        elif density >= 3: r += 1
        if r > 3: self.planet = pg.Planet()
        if random.randint(1,6) + random.randint(1,6) >= 10:
            self.gasGiant = True
    
    def __str__(self):
        return f"Coordinates: {self.coords}\nGas Giant: {self.gasGiant}\nPlanet\n{self.planet}"