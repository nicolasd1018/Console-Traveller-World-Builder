import random
import math
import sys


class Faction:
    strength = 0
    government = 0
    population = 0
    governmentString = ""
    strengthString = ""
    def __init__(self, population):
        self.population = population
        self.strength = self.genStrength()
        self.population = self.genGov()
    
    def genStrength(self):
        s =random.randint(1,6)+random.randint(1,6)
        if s <= 2: self.strengthString = "Obscure group - few have heard of them, no popular support"
        elif s <= 5: self.strengthString = "Fringe group - few supporters"
        elif s <= 7: self.strengthString = "Minor group - some supporters"
        elif s <= 9: self.strengthString = "Notable group - significant support, well known"
        elif s <= 11: self.strengthString = "Significant - nearly as powerful as government"
        else: self.strengthString = "Overwhelming popular support - more powerful than government"
        return s

    def genGov(self):
        while(True):
         g = random.randint(1,6)+random.randint(1,6) - 7 + self.population
         if g != 7: break
        if g <= 0: self.governmentString = "None"
        elif g == 1: self.governmentString = "Company/Corporation"
        elif g == 2: self.governmentString = "Participating Democracy"
        elif g == 3: self.governmentString = "Self-Perpetuating Oligarchy"
        elif g == 4: self.governmentString = "Representative Democracy"
        elif g == 5: self.governmentString = "Feudal Technocracy"
        elif g == 6: self.governmentString = "Captive Government"
        elif g == 7: self.governmentString = "Balkanisation"
        elif g == 8: self.governmentString = "Civil Service Bureaucracy"
        elif g == 9: self.governmentString = "Impersonal Bureaucracy"
        elif g == 10: self.governmentString = "Charismatic Dictator"
        elif g == 11: self.governmentString = "Non-Charismatic Dictator"
        elif g == 12: self.governmentString = "Charismatic Oligarchy"
        elif g == 13: self.governmentString = "Religious Dictatorship"
        elif g == 14: self.governmentString = "Religious Autocracy"
        elif g == 15: self.governmentString = "Totalitarian Oligarchy"
        return g
    
    def __str__(self):
        return f"Ideology: {self.governmentString}\n\t  Strength: {self.strengthString}"

class Starport:
    cost = 0
    fuel = 0
    facilities = 0
    naval = False
    scout = False
    research = False
    tas = False
    _class = 0

    classString = ""
    facilitiesString = ""
    fuelString = ""
    def __init__(self, _class):
        self._class = _class
        self.cost = self.genCost()
        self.facilities = self.genFacilities()
        self.fuel = self.genFuel()
        self.scout = self.genScout()
        self.research = self.genResearch()
        self.naval = self.genNaval()
        self.tas = self.genTas()

    def genCost(self):
        mod = 0
        if self._class == 2: mod =10
        if self._class == 3: mod = 100
        if self._class == 4: mod = 500
        if self._class == 5: mod = 1000
        return random.randint(1,6) * mod

    def genFacilities(self):
        if self._class == 2: 
            self.facilitiesString = "Limited Repair"
            return 1
        if self._class == 3: 
            self.facilitiesString = "Shipyard (small craft)\n\t\t    Repair"
            return 2
        if self._class == 4:
            self.facilitiesString = "Shipyard (spacecraft)\n\t\t    Repair"
            return 3
        if self._class == 5: 
            self.facilitiesString = "Shipyard (all)\n\t\t    Repair"
            return 4
        else: 
            self.facilitiesString = "None"
            return 0

    def genFuel(self):
        if self._class == 0: 
            self.fuelString = "None" 
            return 0
        elif self._class == 1: 
            self.fuelString = "Unrefined"
            return 1
        else: 
            self.fuelString = "Refined" 
            return 2
    
    def genScout(self):
        r = random.randint(1,6) + random.randint(1,6)
        if self._class == 2: 
            if r >= 7: return True
        elif self._class <= 4: 
            if r >= 8: return True
        else: 
            if r >= 10: return True
        return False
    
    def genResearch(self):
        r = random.randint(1,6) + random.randint(1,6)
        if self._class == 5: 
            if r >= 8: return True
        elif self._class <= 3: 
            if r >= 10: return True
        return False

    def genNaval(self):
        r = random.randint(1,6) + random.randint(1,6)
        if self._class >= 3:
            if r >= 8: return True
        return False
    
    def genTas(self):
        r = random.randint(1,6) + random.randint(1,6)
        if self._class >= 4: return True
        elif self._class == 3: 
            if r >= 10: return True
        return False
    
    def __str__(self):
        if self._class == 0: self.classString = "X"
        elif self._class == 1: self.classString = "E"
        elif self._class == 2: self.classString = "D"
        elif self._class == 3: self.classString = "C"
        elif self._class == 4: self.classString = "B"
        elif self._class == 5: self.classString = "A"
        return f"Starport Class: {self.classString}\n\tBerthing Cost: {self.cost}\n\tFacilities: {self.facilitiesString}\n\tFuel: {self.fuelString}\n\tTraveller's Aid Society: {self.tas}\n\tNaval Base: {self.naval}\n\tScout Base: {self.scout}\n\tResearch Base: {self.research}"


class Planet:
    size = 0
    atmosphere = 0
    temperature = 0
    hydrographics = 0 
    population = 0
    government = 0
    factions = []
    culture = ""
    law = 0
    starport = None
    techLevel = 0
    travelCode = 0
    tradeCode = ""
    gravity = 0.0
    name = ""

    spSize = 0
    spAtmosphere = 0.0
    spHydrograpghics = 0
    spPopulation = 0

    atmosphereString = ""
    equipment = ""
    governmentString = ""

    pMap = []

    def __init__(self):
        self.size = self.genSize()
        self.atmosphere = self.genAtmos()
        self.temperature = self.genTemp()
        self.hydrographics = self.genHydro()
        self.population = self.genPop()
        self.government = self.genGov()
        self.genFactions()
        self.culture = self.genCult()
        self.law = self.genLaw()
        self.genStartport()
        self.techLevel = self.genTL()
        self.travelCode = self.genTravelCode()
        self.spSize = self.genSpSize()
        self.atmosphereString = self.genAtmosString()
        self.tradeCode = self.genTradeCode()
        self.pMap = []
    
    def genSize(self):
        return random.randint(1,6)+random.randint(1,6)-2
    
    def genAtmos(self):
        t = random.randint(1,6)+random.randint(1,6)-7+self.size
        if t >= 15:
            t+= random.randint(0,2)
        if t < 0: t = 0
        return t

    def genHydro(self):
        mod = -7
        if self.size <=1: 0
        if self.atmosphere <= 1 or (self.atmosphere >=10 and self.atmosphere<=12): mod -= 4
        else: mod += self.atmosphere
        if self.temperature >= 12: mod -= 6
        elif self.temperature >= 10: mod -= 2
        h = random.randint(1,6)+random.randint(1,6) + mod
        if h < 0: h = 0
        if h == 0: self.spHydrograpghics = random.randint(0,5)
        if h == 1: self.spHydrograpghics = random.randint(6,15)
        if h == 2: self.spHydrograpghics = random.randint(16,25)
        if h == 3: self.spHydrograpghics = random.randint(26,35)
        if h == 4: self.spHydrograpghics = random.randint(36,45)
        if h == 5: self.spHydrograpghics = random.randint(46,55)
        if h == 6: self.spHydrograpghics = random.randint(46,65)
        if h == 7: self.spHydrograpghics = random.randint(66,75)
        if h == 8: self.spHydrograpghics = random.randint(76,85)
        if h == 9: self.spHydrograpghics = random.randint(86,95)
        if h == 10: self.spHydrograpghics = random.randint(96,100)
        return h

    def genTemp(self):
        mod = 0
        if self.atmosphere <= 1: 100
        elif self.atmosphere <= 3: mod = -2
        elif self.atmosphere <= 5 or self.atmosphere == 14: mode = -1
        elif self.atmosphere <= 7: mod = 0
        elif self.atmosphere <= 9: mod = 1
        elif self.atmosphere == 10 and self.atmosphere == 13 and self.atmosphere >= 15: mod = 2
        else: mod = 6
        r = random.randint(1,6)
        if r == 1: mod -= 4
        if r == 6: mod += 4

        return random.randint(1,6)+random.randint(1,6) + mod

    def genPop(self):
        p = random.randint(1,6)+random.randint(1,6) - 2
        i = 0
        while(i < 6 and i < p):
            self.spPopulation += random.randint(0,9)
            self.spPopulation *= 10
            i +=  1
        while(i < p):
            self.spPopulation *= 10
            i += 1
        return p

    def genGov(self):
        if self.population == 0: 
            self.governmentString = "None"
            return 0
        g =random.randint(1,6)+random.randint(1,6)- 7 + self.population
        if g == 0: self.governmentString = "None"
        elif g == 1: self.governmentString = "Company/Corporation"
        elif g == 2: self.governmentString = "Participating Democracy"
        elif g == 3: self.governmentString = "Self-Perpetuating Oligarchy"
        elif g == 4: self.governmentString = "Representative Democracy"
        elif g == 5: self.governmentString = "Feudal Technocracy"
        elif g == 6: self.governmentString = "Captive Government"
        elif g == 7: self.governmentString = "Balkanisation"
        elif g == 8: self.governmentString = "Civil Service Bureaucracy"
        elif g == 9: self.governmentString = "Impersonal Bureaucracy"
        elif g == 10: self.governmentString = "Charismatic Dictator"
        elif g == 11: self.governmentString = "Non-Charismatic Dictator"
        elif g == 12: self.governmentString = "Charismatic Oligarchy"
        elif g == 13: self.governmentString = "Religious Dictatorship"
        elif g == 14: self.governmentString = "Religious Autocracy"
        elif g == 15: self.governmentString = "Totalitarian Oligarchy"
        return g
    
    def genFactions(self):
        n = random.randint(1,3)
        self.factions = []
        if self.government == 0 and self.government == 7:
            n += 1
        elif self.government >= 10: n-=1
        for i in range(n):
            self.factions.append(Faction(self.population))        

    def genCult(self):
        c = ""
        ti = 3
        while(True):
            t = random.randint(1,6)
            o = random.randint(1,6)
            if t == 1: 
                if o == 1: c += "Sexist - one gender is considered subservient or inferior to the other."
                elif o == 2: c = "Religious - culture is heavily influenced by a religion or belief systems, possibly one unique to this world"
                elif o == 3: c = "Artistic - art and culture are highly prized. Aesthetic design is important in all artefacts produced on world."
                elif o == 4: c += "Ritualised - social interaction and trade is highly formalised. Politeness and adherence to traditional forms is considered very important."
                elif o == 5: c += "Conservative - the culture resists change and outside influences."
                elif o == 6: c += "Xenophobic - the culture distrusts outsiders and alien influences. Offworlders will face considerable prejudice."
            elif t == 2:
                if o == 1: c += "Taboo - a particular topic is forbidden and cannot be discussed. Travellers who unwittingly mention this topic will be ostracised."
                elif o == 2: c += "Deceptive - trickery and equivocation are considered acceptable. Honesty is a sign of weakness."
                elif o == 3: c += "Liberal - the culture welcomes change and offworld influence. Travellers who bring new and strange ideas will be welcomed."
                elif o == 4: c += "Honourable - one’s word is one’s bond in the culture. Lying is both rare and despised."
                elif o == 5 and "Influenced - the culture is heavily influenced by another, neighbouring world." not in c: 
                    c += "Influenced - the culture is heavily influencedby another, neighbouring world."
                    #ti = 0
                elif o == 6 and ti >= 3: 
                    c += "Fusion - the culture is a merger of two distinct cultures."
                    ti = 0
            elif t == 3: 
                if o == 1: c += "Barbaric - physical strength and combat prowess are highly valued in the culture. Travellers may be challenged to a fight, or dismissed if they seem incapable of defending themselves. Sports tend towards the bloody and violent."
                elif o == 2: c = "Remnant - the culture is a surviving remnant of a once-great and vibrant civilisation, clinging to its former glory. The world is filled with crumbling ruins, and every story revolves around the good old days."
                elif o == 3: c = "Degenerate - the culture is falling apart and is on the brink of war or economic collapse. Violent protests are common, and the social order is decaying."
                elif o == 4: c += "Progressive - the culture is expanding and vibrant. Fortunes are being made in trade; science is forging bravely ahead."
                elif o == 5: c += "Recovering - a recent trauma, such as a plague, war, disaster or despotic regime has left scars on the culture."
                elif o == 6: c += "Nexus - members of many different cultures and species visit here"
            elif t == 4: 
                if o == 1: c += "Tourist Attraction - some aspect of the culture or the planet draws visitors from all over charted space."
                elif o == 2: c += "Violent - physical conflict is common, taking the form of duels, brawls or other contests. Trial by combat is a part of their judicial system."
                elif o == 3: c += "Peaceful - physical conflict is almost unheard-of. The culture produces few soldiers, and diplomacy reigns supreme. Forceful Travellers will be ostracised."
                elif o == 4: c += "At war - the culture is at war, either with another planet or polity, or is troubled by terrorists or rebels."
                elif o == 5: c += "Obsessed - everyone is obsessed with or addicted to a substance, personality, act or item. This monomania pervades every aspect of the culture."
                elif o == 6: c += "Fashion - fine clothing and decoration are considered vitally important in the culture. Underdressed Travellers have no standing here."
            elif t == 5: 
                if o == 1: c += "Unusual Custom: Offworlders - space travellers hold a unique position in the culture’s mythology or beliefs, and travellers will be expected to live up to these myths"
                elif o == 2: c = "Unusual Custom: Starport - the planet's starport is more than a commercial centre; it might be a religious temple, or be seen as highly controversial and surrounded by protestors."
                elif o == 3: c = "Unusual Custom: Media - news agencies and telecommunications channels are especially strange here. Getting accurate information may be difficult."
                elif o == 4: c += "Unusual Customs: Technology - the culture interacts with technology in an unusual way. Telecommunications might be banned, robots might have civil rights, or cyborgs might be property."
                elif o == 5: c += "Unusual Customs: Lifecycle - there might be a mandatory age of termination, or anagathics might be widely used. Family units might be different, with children being raised by the state or banned in favour of cloning."
                elif o == 6: c += "Unusual Customs: Social Standings - the culture has a distinct caste system. Travellers of a low social standing who do not behave appropriately will face punishment."
            elif t == 6: 
                if o == 1: c += "Unusual Custom: Trade - the culture has an odd attitude towards some aspect of commerce, which may interfere with trade at the spaceport. For example, merchants might expect a gift as part of a deal, or some goods may only be handled by certain families."
                elif o == 2: c = "Unusual Custom: Nobility - those of high social standing have a strange custom associated with them; perhaps nobles are blinded, or must live in gilded cages, or only serve for a single year before being exiled."
                elif o == 3: c = "Unusual Custom: Sex - the culture has an unusual attitude towards intercourse and reproduction. Perhaps cloning is used instead, or sex is used to seal commercial deals."
                elif o == 4: c += "Unusual Customs: Eating - food and drink occupies an unusual place in the culture. Perhaps eating is a private affair, or banquets and formal dinners are seen as the highest form of politeness."
                elif o == 5: c += "Unusual Customs: Travel - travellers may be distrusted or feted, or perhaps the culture frowns on those who leave their homes."
                elif o == 6: c += "Unusual Customs: Conspiracy - something strange is going on. The government is being subverted by another group or agency."
            
            #print(f"{t}, {o}\n {ti}")
            if (t != 2 or o != 5) and ti >= 3: break
            c+="\n\t "
            ti +=1
        return c

    def genLaw(self):
        l = random.randint(1,6)+random.randint(1,6)- 7 + self.government
        if l <= 0: l = 0
        return l

    def genStartport(self):
        r = random.randint(1,6)+random.randint(1,6)
        if self.population >= 10: r += 2
        elif self.population >= 8: r += 1
        elif self.population <= 2: r - 2
        elif self.population <= 4: r -1

        if r <= 2: self.starport = Starport(0)
        elif r <= 4: self.starport = Starport(1)
        elif r <= 6: self.starport = Starport(2)
        elif r <= 8: self.starport = Starport(3)
        elif r <= 10: self.starport = Starport(4)
        else: self.starport =Starport(5)

    def genTL(self):
        r = random.randint(1,6)

        if self.starport._class == 5: r += 6
        elif self.starport._class == 4: r += 4
        elif self.starport._class == 3: r += 2
        elif self.starport._class == 0: r -= 4

        if self.size <= 1: r += 2
        elif self.size <= 4: r += 1
        
        if self.atmosphere <= 3 or self.atmosphere >=10: r += 1

        if self.hydrographics == 0 or self.hydrographics == 9: r += 1
        elif self.hydrographics == 10: r += 2

        if self.population >= 1 and self.population <= 5 or self.population ==8: r += 1
        elif self.population == 9: r += 2
        elif self.population == 10: r += 4

        if self.government == 0 or self.government == 5: r += 1
        elif self.government == 7: r += 2
        elif self.government == 13 or self.government == 14: r -= 2

        return r

    def genTravelCode(self):
        if self.atmosphere >= 10 or self.government == 0 or self.government == 7 or self.government >= 9 or self.law == 0 or self.law >= 9: return 1
        return 0

    def genTradeCode(self):
        t = ""
        if (self.atmosphere >= 4 and self.atmosphere <= 9) and (self.hydrographics >= 4 and self.hydrographics <= 8) and (self.population >= 5 and  self.population <= 7): t += "Ag "
        if self.atmosphere == 0 and self.size == 0 and self.hydrographics == 0: t += "As "
        if self.population == 0 and self.government == 0 and self.law == 0: t += "Ba "
        if self.atmosphere >= 2 and self.hydrographics == 0: t += "De "
        if self.atmosphere >= 10 and self.hydrographics >= 1: t += "Fl "
        if self.size >= 6 and self.size <= 8 and self.atmosphere == 5 or self.atmosphere == 6 or self.atmosphere == 8 and self.hydrographics >= 5 and self.hydrographics <= 7: t += "Ga "
        if self.population >= 9: t += "Hi "
        if self.techLevel >= 12: t += "Ht "
        if self.atmosphere == 0 or self.atmosphere == 1 and self.hydrographics >= 1: t += "Ie "
        if (self.atmosphere >=0 and self.atmosphere <= 2 or self.atmosphere == 4 or self.atmosphere == 7 or self.atmosphere == 9) and self.population >= 9: t += "In "
        if self.population <= 3: t += "Lo "
        if self.techLevel <= 5: t += "Lt "
        if self.atmosphere <= 3 and self.hydrographics <= 3 and self.population >= 6: t += "Na "
        if self.population <= 6: t += "NI "
        if self.atmosphere >= 2 and self.atmosphere <= 5 and self.hydrographics <= 3: t += "Po "
        if self.atmosphere == 6 or self.atmosphere == 8 and self.atmosphere >= 6 and self.atmosphere <= 8 and self.government >= 4 and self.government <=9: t += "Ri "
        if self.atmosphere == 0: t += "Va "
        if self.hydrographics >= 10: t += "Wa "
        return t

    def genSpSize(self):
        if self.size == 0: 500 + random.randint(0, 500)
        elif self.size == 1: 
            self.gravity = 0.05
            return 1600
        elif self.size == 2: 
            self.gravity = 0.15
            return 3200
        elif self.size == 3: 
            self.gravity = 0.25
            return 4800
        elif self.size == 4:
            self.gravity = 0.35
            return 6400
        elif self.size == 5:
            self.gravity = 0.45
            return 8000
        elif self.size == 6:
            self.gravity = 0.7
            return 9600
        elif self.size == 7:
            self.gravity = 0.9
            return 11200
        elif self.size == 8:
            self.gravity = 1.0
            return 12800
        elif self.size == 9:
            self.gravity = 1.25
            return 14400
        elif self.size == 10:
            self.gravity = 1.4
            return 16000
        
    def genAtmosString(self):
        if self.atmosphere == 0:
            self.spAtmosphere = 0
            self.equipment = "Vac Suit Needed"
            return "None"
        if self.atmosphere == 1:
            self.spAtmosphere = random.random()*0.09
            self.equipment = "Vac Suit Needed"
            return "Trace"
        if self.atmosphere == 2:
            self.spAtmosphere = random.randint(10, 42)/100
            self.equipment = "Respirator, Filter Needed"
            return "Very Thin, Tainted"
        if self.atmosphere == 3:
            self.spAtmosphere = random.randint(10, 42)/100
            self.equipment = "Respirator Needed"
            return "Very Thin"
        if self.atmosphere == 4:
            self.spAtmosphere = random.randint(43, 70)/100
            self.equipment = "Filter Needed"
            return "Thin, Tainted"
        if self.atmosphere == 5:
            self.spAtmosphere = random.randint(43, 70)/100
            self.equipment = ""
            return "Thin"
        if self.atmosphere == 6:
            self.spAtmosphere = random.randint(71, 149)/100
            self.equipment = ""
            return "Standard"
        if self.atmosphere == 7:
            self.spAtmosphere = random.randint(71, 149)/100
            self.equipment = "Filter Needed"
            return "Standard, Tainted"
        if self.atmosphere == 8:
            self.spAtmosphere = random.randint(150, 249)/100
            self.equipment = ""
            return "Dense"
        if self.atmosphere == 9:
            self.spAtmosphere = random.randint(150, 249)/100
            self.equipment = "Filter Needed"
            return "Dense, Tainted"
        if self.atmosphere == 10:
            self.spAtmosphere = random.randint(43, 249)/100
            self.equipment = "Air Supply Needed"
            return "Exotic"
        if self.atmosphere == 11:
            self.spAtmosphere = random.randint(43, 400)/100
            self.equipment = "Vac Suit Needed"
            return "Corrosive"
        if self.atmosphere == 12:
            self.spAtmosphere = random.randint(43, 400)/100
            self.equipment = "Vac Suit Needed"
            return "Insidious"
        if self.atmosphere == 13:
            self.spAtmosphere = random.randint(250, 600)/100
            self.equipment = ""
            return "Very Dense"
        if self.atmosphere == 15:
            self.spAtmosphere = 1.0
            self.equipment = ""
            return "Ellipsoidal"
        if self.atmosphere == 16:
            self.spAtmosphere = 4.0
            self.equipment = ""
            return "Panthalassic"
        if self.atmosphere == 17:
            self.spAtmosphere = 1.0
            self.equipment = ""
            return "Extreme Weather"
        
    def setName(self, name):
        self.name = name

    def genMap(self):
        for i in range(40):
            self.pMap.append([])
            for j in range(100):
                if random.randint(1,100) > self.spHydrograpghics:
                    self.pMap[i].append("This hex is composed largely of land.")
                else: 
                    self.pMap[i].append("This hex is composed largely of water.")


    def __str__(self):
        factionString = ""
        for i in self.factions:
            factionString += f"{i}\n\t  "
        travelCode = ""
        if self.travelCode == 1: travelCode = "Amber"
        return f"Name: {self.name}\nStarport: \n\t{self.starport}\nSize: {self.size} ({self.spSize})\nGravity: {self.gravity}\nAtmosphere: {self.atmosphere} ({self.atmosphereString}, {self.spAtmosphere}) {self.equipment}\nHydrographics: {self.hydrographics} ({self.spHydrograpghics}%)\nPopulation: {self.population} ({self.spPopulation})\nGovernment: {self.governmentString}\nFactions: {factionString}\nLaw Level: {self.law}\nTech Level: {self.techLevel}\nTrade Codes: {self.tradeCode}\nTravel Code: {travelCode}\nCulture: {self.culture}"
    
