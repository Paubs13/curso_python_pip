import utils
import read_csv
import charts

data = read_csv.read_csv('data.csv')

country = input('Type Country => ')
country_name = country

if(country == 'World'):
  continent = input('Type Continent: => ')
  continent_name = continent
  names, values = utils.population_percentage(continent)
  charts.generate_pie(continent_name, names, values)
  print('Chart has been generated succesfully!')
else:
  result = utils.filter_country(country)
  if len(result) > 0:
    labels, values = utils.get_population(result)
    charts.generate_chart (country_name, labels, values)
    print('Chart has been generated succesfully!')
    



  




