import pandas as pd
from Properties import properties, railroads, panda_of_placements
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class Property:
    def __init__(self, name, price, price_per_house, rent, rent1, rent2, rent3, rent4, rent_hotel, mortgage,
                 placement):
        self.name = name
        self.price = price
        self.price_per_house = price_per_house
        self.rent_base = rent
        self.rent_one_house = rent1
        self.rent_two_houses = rent2
        self.rent_three_houses = rent3
        self.rent_four_houses = rent4
        self.rent_for_hotel = rent_hotel
        self.mortgage = mortgage
        self.position = placement


class Railroads:
    def __init__(self, name, price, rent, position):
        self.name = name
        self.price = price
        self.price_per_house = rent
        self.rent_base = position


class WaterWorks:
    def __init__(self):
        self.name = "Water Works"
        self.price = 150
        self.position = 29


class ElectricCompany:
    def __init__(self):
        self.name = 'Electric Company'
        self.price = 150
        self.position = 13


class IncomeTax:
    def __init__(self):
        self.name = 'Income Tax'
        self.position = 5


class LuxuryTax:
    def __init__(self):
        self.name = 'Luxury Tax'
        self.position = 39


class Go:
    def __init__(self):
        self.name = 'Go'
        self.position = 1


class Jail:
    def __init__(self):
        self.name = 'Jail'
        self.placement = 11


class GoToJail:
    def __init__(self):
        self.name = 'Go To Jail'
        self.placement = 31


class CommunityChest:
    def __init__(self):
        self.name = 'Community Chest'
        self.placement = [3, 18, 34]


class Chance:
    def __init__(self):
        self.name = 'Chance'
        self.placement = [8, 23, 37]


list_of_placements = [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 33, 35, 38, 40]
list_of_properties_class = []
list_of_properties = properties['Name'].tolist()
dict_of_props = {}
dict_of_rail = {}

for i in range(properties.index.size):
    dict_of_props[list_of_placements[i]] = (Property(properties.iloc[i, 0], properties.iloc[i, 1],
                                            properties.iloc[i, 2],  properties.iloc[i, 3],
                                            properties.iloc[i, 4], properties.iloc[i, 5],
                                            properties.iloc[i, 6], properties.iloc[i, 7],
                                            properties.iloc[i, 8],  properties.iloc[i, 9], list_of_placements[i]))

for i in range(railroads.index.size):
    dict_of_rail[railroads.iloc[i, 3]] = (Railroads(railroads.iloc[i, 0], railroads.iloc[i, 1],
                                          railroads.iloc[i, 2],  railroads.iloc[i, 3]))

water_works = WaterWorks()

electric_company = ElectricCompany()

income_tax = IncomeTax()

luxury_tax = LuxuryTax()

go = Go()

jail = Jail()

go_to_jail = GoToJail()

community_chest = CommunityChest()

chance = Chance()









