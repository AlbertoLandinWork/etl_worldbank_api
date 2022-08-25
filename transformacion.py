import pandas as pd

data_frame = pd.read_csv('./Data/raw_data.csv')

data_frame.drop(columns = ['Unnamed: 0', 'unit', 'obs_status', 'decimal'])
data_frame.rename(columns = {'countryiso3code':'country_code', 'value': 'population', 'date': 'year'}, inplace = True)
data_frame.drop(columns = 'old_index', inplace = True)

data_frame.to_csv('./Data/population.csv')