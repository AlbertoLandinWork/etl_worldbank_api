import pandas as pd


def transform(path: str)-> pd.DataFrame:
    data_frame = pd.read_csv(path)


    data_frame.drop(columns = ['unit', 'obs_status', 'decimal'], inplace = True)
    data_frame.rename(columns = {'countryiso3code':'country_code', 'value': 'population', 'date': 'year'}, inplace = True)
    data_frame.dropna(subset = ['country_code', 'population'], inplace = True)


    return data_frame