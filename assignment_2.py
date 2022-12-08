import pandas as pd
import matplotlib.pyplot as plt


def get_data(file_name, indicator):
    
    """
    Reading World Bank Climate data to analyze how the 
    climate change afftect the total popultaion, 
    Urban population and Aggricultural land
    """
    
    df = pd.read_csv(file_name, index_col=False)
    df = df[df['Indicator Name'] == indicator]
    df.drop(['Country Code', 'Indicator Code', 'Indicator Name'],
                axis=1, inplace=True)
    
    country = ['Australia', 'Bangladesh', 'Germany', 
               'United Kingdom','India', 'Pakistan']
    
#     filter cities
    df= df[df['Country Name'].isin(country)]
    
    year_as_column = df.set_index('Country Name')
    country_as_column = year_as_column.T
    return year_as_column.reset_index(), country_as_column


def compare_urban_population_growth():
    
    population_grwoth = get_data("API_19_DS2_en_csv_v2_4700503" \
                  "/API_19_DS2_en_csv_v2_4700503.csv", \
                  "Urban population (% of total population)" )[1]
    
    
    years = list(population_grwoth.reset_index()['index'][40:])
    print(years)
    
    countries = list(population_grwoth.columns)
    print(countries)
    
    f = plt.figure()
    f.set_figwidth(20)
    f.set_figheight(5)
    
    for country in countries:
        plt.plot(years, list(population_grwoth[country][40:]), '', label = country )
    
#     plt.figure(figsize=(18, 18))
    plt.legend()
    plt.show()

compare_urban_population_growth()


def compare_agriculter_land_growth():

    """
    comparing agricultural land of developed and under deveopled 
    countriies
    """
    
    agriculture_land_growth = get_data("API_19_DS2_en_csv_v2_4700503" \
                  "/API_19_DS2_en_csv_v2_4700503.csv", \
                  "Agricultural land (% of land area)" )[1]
    
    
    years = list(agriculture_land_growth.reset_index()['index'][40:])
    print(years)
    
    countries = list(agriculture_land_growth.columns)
    print(countries)
    
    f = plt.figure()
    f.set_figwidth(20)
    f.set_figheight(5)
    
    for country in countries:
        plt.plot(years, list(agriculture_land_growth[country][40:]), '', label = country )
    
#     plt.figure(figsize=(18, 18))
    plt.legend()
    plt.show()


compare_agriculter_land_growth()


def compare_urban_population_with_agriculture_land():

    """
    compare all the countries agricultiral land with own urban 
    population growth %
    """
    
    population_grwoth = get_data("API_19_DS2_en_csv_v2_4700503" \
                  "/API_19_DS2_en_csv_v2_4700503.csv", \
                  "Urban population (% of total population)" )[1]
    
    agriculture_land_growth = get_data("API_19_DS2_en_csv_v2_4700503" \
                  "/API_19_DS2_en_csv_v2_4700503.csv", \
                  "Agricultural land (% of land area)" )[1]
    
    years = list(population_grwoth.reset_index()['index'][40:])
    
    countries = list(population_grwoth.columns)
    
    for country in countries:
        f = plt.figure()
        f.set_figwidth(20)
        f.set_figheight(5)
        plt.plot(years, list(population_grwoth[country][40:]), '', 
                     label = "Urban population (% of total population" )
        plt.plot(years, list(agriculture_land_growth[country][40:]), '', 
                        label = "Agricultural land (% of land area)" )
        plt.title(country)
        plt.legend()
        plt.show()
    
#     plt.figure(figsize=(18, 18))
    
compare_urban_population_with_agriculture_land()
