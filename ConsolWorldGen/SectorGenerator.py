from pathlib import Path
import random
import sys
sys.path.append('../Traveller Programs')
import SubsectorGenerator as sug

class Sector:
    subsectorList = []
    name = ""
    def __init__(self, name):
        self.name = name
        p = random.randint(0,3)
        for i in range(4):
            self.subsectorList.append([])
            for j in range(4):
                print(p)
                self.subsectorList[i].append(sug.Subsector(f"0{i+1}0{j+1}",p))
                p = (p +random.randint(0,3)) // 2

    def getSubsector(self, x, y):
        return self.subsectorList[x][y]

    def __str__(self):
        map = "0101 0102 0103 0104\n0201 0202 0203 0204\n0301 0302 0303 0304\n0401 0402 0403 0404"
        return f"Name: {self.name}\n\n{map}"
