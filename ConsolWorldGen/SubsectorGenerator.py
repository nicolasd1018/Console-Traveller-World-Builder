import random
from pathlib import Path
import sys
#import numpy
sys.path.append('../Traveller Programs')
import SystemGenerator as sg

class Subsector:
    population = 2
    coords = ""
    sysArray = []
    def __init__(self, coords, population):
        self.population = population
        self.coords = coords
        self.sysArray = []
        for i in range(8):
            self.sysArray.append([])
            for j in range(10):
                cstr = f"0{i+1}"
                if j < 9:
                    cstr += f"0{j+1}"
                else: cstr += str(10)
                self.sysArray[i].append(sg.System(population, cstr))
        print(f"Coord: {coords} {len(self.sysArray)}")
    
    def getSystem(self,x,y):
        print(f"{x},{y}")
        return self.sysArray[x][y]
    
    def genRelevantOnly(self):
        map = ""
        for i in self.sysArray:
            map += "\n"
            for j in i:
                if j.planet == None:
                    map += "---- "
                else: map += f"{j.coords} "
        return map

    def __str__(self, rel):
        spop = ""
        if self.population == 0: spop = "Rift"
        elif self.population == 1: spop = "Sparse"
        elif self.population == 2: spop = "Normal"
        else: spop = "Dense"
        map = ""
        if not rel:
            for i in range(8):
                map += "\n"
                for j in range(10):
                    map += f"{self.sysArray[i][j].coords} "
        else: map = self.genRelevantOnly()
        return f"Coordinates: {self.coords}\nPopulation Density: {spop}\n{map}"


