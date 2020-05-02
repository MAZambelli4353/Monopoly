import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

properties = pd.read_csv("Monopoly_Properties.csv")
cols = [0]
properties.drop(properties.columns[cols], axis=1, inplace=True)
properties.drop(properties.columns[cols], axis=1, inplace=True)

railroads = pd.DataFrame({'Name': ['Reading Railroad', 'Pennsylvania Railroad', 'B. & O. Railroad',
                          'Short Line Railroad'], 'Price': [200, 200, 200, 200],
                          'Rent': [25, 25, 25, 25], 'Placement': [6, 16, 26, 36]})


dict_of_placements = {'dict_of_props': [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 33, 35,
                      38, 40], 'dict_of_rail': [6, 16, 26, 36], 'water_works': 29, 'electric_company':
                      13, 'go': 1, 'community_chest': [3, 18, 34], 'chance': [8, 23, 37], 'income_tax'
                      : 5, 'luxury_tax': 39, 'jail': 11, 'free_parking': 21, 'go_to_jail': 31}

panda_of_placements = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in dict_of_placements.items()])).fillna(0)
panda_of_placements = panda_of_placements.astype(int)
