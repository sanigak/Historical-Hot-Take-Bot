import random


def IntroGenerator():
    chance = random.randint(1,4)
    if chance > 1:
        input = open("input\Intros.txt","r")
        list = input.readlines()
        intro = random.choice(list).rstrip()
        return intro
    else:
        input1 = open("input\Historians.txt","r")
        list1 = input1.readlines()
        hist = random.choice(list1).rstrip()
        input2 = open("input\HistoriansModifiers.txt","r")
        list2 = input2.readlines()
        phrase = random.choice(list2).rstrip()
        ans = phrase.replace("BLANK",hist)
        return ans


#SUBECTS
def CountryGenerator():
    input = open("input\Countries.txt","r")
    list = input.readlines()
    country = random.choice(list).rstrip()
    return country

def PeopleOfCountryGenerator():
    input = open("input\Countries.txt","r")
    list = input.readlines()
    country = random.choice(list).rstrip()
    people = "The People of " + country
    return people

def CurrencyGenerator():
    input = open("input\Currencies.txt","r")
    list = input.readlines()
    currency = random.choice(list).rstrip()
    currency = "The " + currency
    return currency

def CurrencyGeneratorMod():
    input = open("input\CurrenciesModifiers.txt","r")
    list = input.readlines()
    mod = random.choice(list).rstrip()
    currency = CurrencyGenerator()
    currencyMod = mod + " " + currency
    return currencyMod

def EmpireGenerator():
    input = open("input\Empires.txt","r")
    list = input.readlines()
    empire = random.choice(list).rstrip()
    empire = "the " + empire
    return empire

def EmpireGeneratorMod():
    input = open("input\EmpiresModifiers.txt","r")
    list = input.readlines()
    mod = random.choice(list).rstrip()
    empire = EmpireGenerator()
    empireMod = mod + " " + empire
    return empireMod

def HistorianGenerator():
    input = open("input\Historians.txt","r")
    list = input.readlines()
    historian = random.choice(list).rstrip()
    return historian

def IndustryGenerator():
    input = open("input\Industries.txt","r")
    list = input.readlines()
    industry = random.choice(list).rstrip()
    industry = "the " + industry + " industry"
    return industry

def ComplexGenerator():

    input = open("input\Industries.txt","r")
    list = input.readlines()
    first = random.choice(list).rstrip()
    second = random.choice(list).rstrip()
    complex = "the " + first + "-" + second + "-complex"
    return complex

def MonarchGenerator():
    input = open("input\Monarchs.txt","r")
    list = input.readlines()
    monarch = random.choice(list).rstrip()
    return monarch

def MonarchyGenerator():
    input = open("input\Monarchs.txt","r")
    list = input.readlines()
    monarch = random.choice(list).rstrip()
    monarch = "the reign of " + monarch
    return monarch

def PresidentGenerator():

    input = open("input\Presidents.txt","r")
    list = input.readlines()
    pres = random.choice(list).rstrip()
    return pres

def PresidencyGenerator():

    input = open("input\Presidents.txt","r")
    list = input.readlines()
    pres = random.choice(list).rstrip()
    presidency = "the Presidency of " + pres
    return presidency

def PremiershipGenerator():
    input = open("input\PresidentsButCanada.txt","r")
    list = input.readlines()
    prem = random.choice(list).rstrip()
    premship = "the Premiership of " + prem
    return premship

def TimeGenerator():
    input = open("input\TimePeriods.txt","r")
    list = input.readlines()
    time = random.choice(list).rstrip()
    return time

def WarGenerator():
    input = open("input\Wars.txt","r")
    list = input.readlines()
    war = random.choice(list).rstrip()
    war = "The " + war
    return war

def WarGeneratorMod():
    input = open("input\WarsModifiers.txt","r")
    list = input.readlines()
    mod = random.choice(list).rstrip()
    war = WarGenerator()
    warMod = mod + " " + war
    return warMod




def RandSubject1():
    listy = []
    #listy.append(CountryGenerator())
    #listy.append(PeopleOfCountryGenerator())
    #listy.append(CurrencyGenerator())
    listy.append(CurrencyGeneratorMod())
    #listy.append(EmpireGenerator())
    listy.append(EmpireGeneratorMod())
    #listy.append(HistorianGenerator())
    #listy.append(IndustryGenerator())
    #listy.append(ComplexGenerator())
    #listy.append(MonarchGenerator())
    listy.append(MonarchyGenerator())
    #listy.append(PresidentGenerator())
    listy.append(PresidencyGenerator())
    listy.append(PremiershipGenerator())
    listy.append(TimeGenerator())
    listy.append(WarGenerator())
    listy.append(WarGeneratorMod())
    subject = random.choice(listy)
    return subject

def RandSubject2():
    listy = []
    listy.append(CountryGenerator())
    listy.append(PeopleOfCountryGenerator())
    #listy.append(CurrencyGenerator())
    #listy.append(CurrencyGeneratorMod())
    listy.append(EmpireGenerator())
    #listy.append(EmpireGeneratorMod())
    #listy.append(HistorianGenerator())
    listy.append(IndustryGenerator())
    listy.append(ComplexGenerator())
    listy.append(MonarchGenerator())
    #listy.append(MonarchyGenerator())
    listy.append(PresidentGenerator())
    #listy.append(PresidencyGenerator())
    #listy.append(PremiershipGenerator())
    #listy.append(TimeGenerator())
    #listy.append(WarGenerator())
    #listy.append(WarGeneratorMod())
    subject = random.choice(listy)
    return subject

#Descriptors
def GoodBadGenerator():
    input = open("input\Adjectives.txt","r")
    list = input.readlines()
    adj = random.choice(list).rstrip()
    return adj

def AdverbGenerator():
    input = open("input\Adverbs.txt","r")
    list = input.readlines()
    adv = random.choice(list).rstrip()
    return adv

def AdvAdjGenerator():
    adj = GoodBadGenerator()
    adv = AdverbGenerator()
    ans = adv + " " + adj
    return ans






def GenerateHotTake():
    intro = IntroGenerator()
    sub1 = RandSubject1()
    sub2 = RandSubject2()
    advadj = AdvAdjGenerator()

    ans = intro + " " + sub1 + " was " + advadj + " for " + sub2
    return ans


take = GenerateHotTake()

print(take)
