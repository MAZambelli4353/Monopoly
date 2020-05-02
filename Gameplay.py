from Classes_Of_Properties import dict_of_props, dict_of_rail, water_works, electric_company
from Properties import panda_of_placements
import random
import pandas


class Player:
    def __init__(self, name):
        self.name = name
        self.bank = 200
        self.properties = []
        self.cards = []
        self.placement = 0


player = Player('Mark')


while True:
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    move = dice_one + dice_two
    for column in panda_of_placements:
        if move in column:
            print(column)
            col = column
        else:
            continue
    print(str(col))
    name = panda_of_placements(column=col)
    break


