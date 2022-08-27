from extract import extract
from transform import transform


path = 'https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?page=1&format=json'
path2 = './Data/raw_data.csv'


def run():
    data_frame = extract(path)
    data_frame.to_csv('./Data/raw_data.csv', index = False)

    data_frame = transform(path2)
    data_frame.to_csv('./Data/population.csv', index = False)


if __name__ == '__main__':
    run()