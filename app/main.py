import utils
import read_csv
import charts
import pandas as pd

#data = read_csv.read_csv('data.csv')

country = input('Type Country => ')
country_name = country
df = pd.read_csv('data.csv')

if(country == 'World'):
  continent = input('Type Continent: => ')
  continent_name = continent
  #names, values = utils.population_percentage(continent)

  df = df[df['Continent'] == continent]
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie(continent_name, countries, percentages)
  print('Chart has been generated succesfully!')
else:
  result = utils.filter_country(country)
  if len(result) > 0:
   labels, values = utils.get_population(result)
   
   charts.generate_chart (country_name, labels, values)
   print('Chart has been generated succesfully!')
    



  




