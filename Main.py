from pathlib import Path
import sys
import pickle
sys.path.append('../Traveller Programs')
import PlanetGenerator as pg
import SystemGenerator as sg
import SubsectorGenerator as sug
import SectorGenerator as seg
import os
import os.path
import random
def loadall(f):
    while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

def loadSubsector(f):
    i = 0
    suList = []
    while True:
            try:
                if i == 0:
                    suList.append(pickle.load(f))
                    i =1
                else: 
                    suList[len(suList)-1].sysArray = pickle.load(f)
                    i =0
            except EOFError:
                break
    return suList

def loadSector(f):
    i = 0
    seList = []
    while True:
            try:
                l = pickle.load(f)
                if type(l) == type(seg.Sector("")):
                    seList.append(l)
            except EOFError:
                break
    return seList



while(True):
    print("Menu\n1. Generate Planet\n2. Load Planet\n3. Generate System\n4. Load System\n5. Generate Subsector\n6. Load Subsectors\n7. Generate Sector\n8. Load Sector \n0. Exit")
    i = int(input())
    if i == 1:
        go = True
        while(go):
            go = True
            p = pg.Planet()
            print(p)
            print("\nWould you like to save this Planet? y/n")
            a = input()
            if a == "y":
                print("Please name the planet.")
                n = input()
                p.setName(n)
                f = open("./savedFiles/planets.pkl","ab")
                pickle.dump(p, f)
                f.close()
                print("Would you like to generate a different planet? y/n")
                b = input()
                if b == "n": go = False
            else:
                print("Would you like to generate a different planet? y/n")
                a = input()
                if a == "n": go = False
    elif i == 2: 
        if os.path.exists("./savedFiles/planets.pkl"):
            f = open("./savedFiles/planets.pkl","rb")
            pArr = list(loadall(f))
            n = 1
            print("\nPlanet List")
            for i in pArr:
                print(f"{n}. {i.name}")
                n += 1
            print("\nPick a planet.")
            a = int(input())
            if a > len(pArr):
                print("That planet is unavailable. Please pick another.")
            else:
                p = pArr[a-1]
                print(p)
                x = input("Would you like to delete this planet? y/n ")
                if x == "y":
                    del pArr[a-1]
                    f.close()
                    if pArr != []:
                        f = open("./savedFiles/planets.pkl","wb")
                        pickle.dump(pArr[0], f)
                        f.close()
                        f = open("./savedFiles/planets.pkl","ab")
                        for i in pArr[1:]:
                            pickle.dump(i, f)
                        f.close()
                    else:
                        os.remove("./savedFiles/planets.pkl")
        else: print("There are no planets saved.")
    elif i == 3:
        go = True
        while(go):
            go = True
            coords = input("Input coordinates(ex. 0101) ")
            density = int(input("Input population density(0 - rift, 1 - sparse, 2 - normal, 3 - populous)"))
            s = sg.System(density, coords)
            print(s)
            print("\nWould you like to save this system? y/n")
            a = input()
            if a == "y":
                if (s.planet != None):
                    print("Please name the system's planet.")
                    n = input()
                    s.planet.setName(n)
                f = open("./savedFiles/systems.pkl","ab")
                pickle.dump(s, f)
                f.close()
                b = input("Would you like to generate another system? y/n ")
                if b != "y":
                    go = False
            else:
                print("Would you like to generate a different system? y/n")
                a = input()
                if a == "n": go = False
    elif i == 4:
        if os.path.exists("./savedFiles/systems.pkl"):
            f = open("./savedFiles/systems.pkl","rb")
            sArr = list(loadall(f))
            if sArr != []:
                n = 1
                print("Systems List")
                for i in sArr:
                    print(f"{n}. {i.coords}")
                    n += 1
                print("\nPick a system.")
                a = int(input())
                s = sArr[a-1]
                print(s)
                x = input("Would you like to delete this system? y/n ")
                if x == "y":
                    del sArr[a-1]
                    f.close()
                    if sArr != []:
                        f = open("./savedFiles/systems.pkl","wb")
                        pickle.dump(sArr[0], f)
                        f.close()
                        f = open("./savedFiles/systems.pkl","ab")
                        for i in sArr[1:]:
                            pickle.dump(i, f)
                        f.close()
                    else: os.remove("./savedFiles/systems.pkl")
            else: print("There are no systems saved.")
        else: print("There are no systems saved.")
    elif i == 5: 
        go = True
        while(go):
            density = int(input("Input population density(0 - rift, 1 - sparse, 2 - normal, 3 - populous)"))
            su = sug.Subsector("0101",density)
            go1 = True
            while(go1):
                print(su.__str__(False))
                d = input("Would you like to show only populated systems? y/n ")
                if d == "y":
                    print(su.__str__(True))
                a = input("Would you like to explore the sector? y/n ")
                if a == "y":
                    x = int(input("Input the X coordinate(ex. 1): "))
                    y = int(input("Input the Y coordinate(ex. 1): "))
                    s = su.getSystem(x-1,y-1)
                    print(s)
                    if s.planet != None:
                        b = input("Would you like to name this planet? y/n ")
                        if b == "y":
                            n = input("Input Name: ")
                            s.planet.name = n
                else: go1 = False
            a = input("Would you like to save this subsector? y/n ")
            if a == "y":
                f = open("./savedFiles/subsectors.pkl","ab")
                pickle.dump(su, f)
                pickle.dump(su.sysArray, f)
                f.close()
            a = input("Would you like to generate another subsector? y/n ")
            if a != "y":
                go = False
    elif i == 6:
        if os.path.exists("./savedFiles/subsectors.pkl"):
            f = open("./savedFiles/subsectors.pkl","rb")
            suArr = list(loadSubsector(f))
            if suArr != []:
                n = 1
                print("Subsectors List")
                for i in suArr:
                    print(f"{n}. {i.coords}")
                    n += 1
                print("\nPick a subsector.")
                a = int(input())
                go = True
                while(go):
                    # print(a)
                    su = suArr[a-1]
                    print(su.__str__(False))
                    d = input("Would you like to show only populated systems? y/n ")
                    if d == "y":
                        print(su.__str__(True))
                    b = input("Would you like to explore the subsector? y/n ")
                    if b == "y":
                        x = int(input("Input the X coordinate(ex. 1): "))
                        y = int(input("Input the Y coordinate(ex. 1): "))
                        s = su.getSystem(x-1,y-1)
                        print(s)
                        if s.planet != None:
                            c = input("Would you like to name this planet? y/n ")
                            if c == "y":
                                s.planet.name = input("Please name the planet. ")
                    else: go =False

                x = input("Would you like to delete this subsector? y/n ")
                if x == "y":
                    del suArr[a-1]
                    f.close()
                    if suArr != []:
                        f = open("./savedFiles/subsectors.pkl","wb")
                        pickle.dump(suArr[0], f)
                        f.close()
                        f = open("./savedFiles/subsectors.pkl","ab")
                        for i in suArr[1:]:
                            pickle.dump(i, f)
                        f.close()
                    else: os.remove("./savedFiles/subsectors.pkl")
            else: print("There are no subsectors saved.")
        else: print("There are no subsectors saved.")
    elif i == 7:
        go = True
        while(go):
            go = True
            n = input("Please name the sector. ")
            se = seg.Sector(n)
            go1 = True
            while(go1):
                print(se)
                a = input("\nWould you like to explore this sector? y/n ")
                if a == "y":
                    x = int(input("Input the X coordinate(ex. 1): "))
                    y = int(input("Input the Y coordinate(ex. 1): "))
                    su = se.getSubsector(x-1,y-1)
                    go2 = True
                    while(go2):
                        print(su.__str__(False))
                        d = input("Would you like to show only populated systems? y/n ")
                        if d == "y":
                            print(su.__str__(True))
                        b = input("\nWould you like to explore this subsector? y/n ")
                        if b == "y":
                            x = int(input("Input the X coordinate(ex. 1): "))
                            y = int(input("Input the Y coordinate(ex. 1): "))
                            s = su.getSystem(x-1,y-1)
                            print(s)
                            if s.planet != None:
                                c = input("Would you like to name this planet? y/n ")
                                if c == "y":
                                    s.planet.name = input("Input Name: ")
                        else: go2 = False
                else: go1 = False
            a = input("\nWould you like to save this sector? y/n ")
            if a == "y":
                f = open("./savedFiles/sectors.pkl","ab")
                pickle.dump(se, f)
                pickle.dump(se.subsectorList,f)
                for i in se.subsectorList:
                    pickle.dump(i, f)
                f.close()
            
            print("Would you like to generate a different sector? y/n")
            a = input()
            if a == "n": go = False
    elif i == 8:
        if os.path.exists("./savedFiles/sectors.pkl"):
            f = open("./savedFiles/sectors.pkl","rb")
            seArr = list(loadSector(f))
            if seArr != []:
                n = 1
                print("Sectors List")
                for i in range(len(seArr)):
                    print(f"{n}. {seArr[i].name}")
                    n += 1
                print("\nPick a sector.")
                a = int(input())
                go = True
                while(go):
                    print(a)
                    se = seArr[a-1]
                    print(se)
                    b = input("Would you like to explore the sector? y/n ")
                    if b == "y":
                        x = int(input("Input the X coordinate(ex. 1): "))
                        y = int(input("Input the Y coordinate(ex. 1): "))
                        su = se.getSubsector(x-1,y-1)
                        go1 = True
                        while(go1):
                            print(su.__str__(False))
                            d = input("Would you like to show only populated systems? y/n ")
                            if d == "y":
                                print(su.__str__(True))
                            c = input("Would you like to explore the subsector? y/n ")
                            if c == "y":
                                x = int(input("Input the X coordinate(ex. 1): "))
                                y = int(input("Input the Y coordinate(ex. 1): "))
                                s = su.getSystem(x-1,y-1)
                                print(s)
                                if s.planet != None:
                                    d = "Would you like to name the planet? y/n "
                                    if d == "y":
                                        s.planet.name = input("Input Name: ")
                            else: go1 = False
                    else: go =False

                x = input("Would you like to delete this sector? y/n ")
                if x == "y":
                    del seArr[a-1]
                    f.close()
                    if seArr != []:
                        f = open("./savedFiles/sectors.pkl","wb")
                        pickle.dump(suArr[0], f)
                        f.close()
                        f = open("./savedFiles/sectors.pkl","ab")
                        for i in sArr[1:]:
                            pickle.dump(i, f)
                        f.close()
                    else: os.remove("./savedFiles/sectors.pkl")
            else: print("There are no sectors saved.")
        else: print("There are no sectors saved.")
    elif i == 0: break
