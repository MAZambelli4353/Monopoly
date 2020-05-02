import requests
import json
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
from pandas.io.html import read_html


'''Getting property data'''
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
url = "http://www.falstad.com/monopoly.html"
df = pd.read_html(url, header=0)
df1 = df[0]
df1.to_csv('Monopoly_Properties.csv')
print(df1)

'''                      '''

