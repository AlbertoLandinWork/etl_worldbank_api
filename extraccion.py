import numpy as np
import pandas as pd
import json
import requests


"""
Hago una solicitud preliminar a la api, extraigo el total de páginas y
preparo las variables que necesito para la extracción completa de los datos.
"""
response = requests.get(f'https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?page={1}&format=json')
total_pages = response.json()[0]['pages']
page = 1
data_frame = pd.DataFrame()


"""
Realizo la solicitud y convierto los datos a un objeto DataFrame.
""" 
while page <= total_pages:
    response = requests.get(f'https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?page={page}&format=json')
    df = pd.DataFrame(response.json()[1], columns = ['country_name', 'countryiso3code', 'date', 'value', 'unit', 'obs_status', 'decimal'])
    df['country_name'] = response.json()[1][0]['country']['value']
    data_frame = pd.concat([data_frame, df], axis = 0)
    page += 1


"""
Almaceno los datos en un csv.
"""
data_frame.to_csv('./Data/raw_data.csv')