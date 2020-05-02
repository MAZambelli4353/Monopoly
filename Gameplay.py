from Classes_Of_Properties import dict_of_props, dict_of_rail, water_works, electric_company, go, go_to_jail, chance, community_chest, income_tax, luxury_tax, jail

from Properties import panda_of_placements
import random
import pandas as pd


class Player:
    def __init__(self, name):
        self.name = name
        self.bank = 2000000
        self.properties = []
        self.cards = []
        self.placement = 0


player = Player('Mark')
placement_on_board = 1
buyable_in_dict = ['dict_of_props', 'dict_of_rail']
buyable = ['water_works', 'electric_company']
charges = ['income_tax', 'luxury_tax']


def get_right_pool(roll):
    x = pd.DataFrame(panda_of_placements)
    x = x == roll
    list_of_column_names = x.keys()
    for column in list_of_column_names:
        if any(x[column]):
            name_of_dictionary = column
            return name_of_dictionary
        else:
            continue


def roll_dice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    num = dice_one + dice_two
    return num


def bank(player_bank_account, property_amount):
    if player_bank_account >= property_amount:
        return True
    else:
        return False


def other_landing_spots():
    x = 'You did not land on a property'
    return x


m = 105

while m > 0:

    placement_on_board += roll_dice()

    '''Gets the dictionary name based on positioning.'''
    type_of_property = get_right_pool(placement_on_board)
    print(type_of_property)
    print(placement_on_board)

    flag = 0

    '''Testing to see if I landed on a buy-able property and can afford it.'''
    if type_of_property in buyable_in_dict:
        can_you_afford = bank(player.bank, eval(type_of_property)[placement_on_board].price)
        flag = 1
    elif type_of_property in buyable:
        can_you_afford = bank(player.bank, eval(type_of_property).price)
        flag = 2
    elif type_of_property in charges:
        can_you_afford = bank(player.bank, eval(type_of_property).cost)
        flag = 3
    else:
        can_you_afford = other_landing_spots()
        flag = 4

    if flag == 1 and can_you_afford:
        option = input("Do you want to buy the property for " + str(eval(type_of_property)[placement_on_board].price)
                       + "?")
        if option == 'yes':
            player.bank -= eval(type_of_property)[placement_on_board].price
            print("You now have " + str(player.bank) + ' dollars left in your bank.')
        else:
            print("You decided to not buy this property.")
    if flag == 2 and can_you_afford:
        option = input("Do you want to buy the property for " + str(eval(type_of_property)[placement_on_board].price)
                       + "?")
        if option == 'yes' or 'y':
            player.bank -= eval(type_of_property).price
            print("You now have " + str(player.bank) + ' dollars left in your bank.')
        else:
            print("You decided to not buy this property.")
    if flag == 3 and can_you_afford:
        player.bank -= eval(type_of_property).cost
        print("You were charges tax, you now have " + str(player.bank) + ' in your bank account.')
    if flag == 4:
        print("you landed on a special spot.  I will deal with this later.")

    m -= 1


