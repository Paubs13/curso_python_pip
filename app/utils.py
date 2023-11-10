def filter_country(country):
  from read_csv import read_csv
  data = read_csv('data.csv')
  the_list = list(filter(lambda item: item ['Country/Territory'] == country, data))
  return the_list
  
def get_population(a_list):
  new_dict = {}
    
  for key, value in a_list[0].items():
    
    if key[-10:] == 'Population':
      new_dict[key[0:4]] = int(value)
      labels = new_dict.keys()
      values = new_dict.values()
    
  return labels, values

def population_percentage(continent):
  
  from read_csv import read_csv
  data = read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == continent, data))
  
  percentages_dict = {item['Country/Territory']: item ['World Population Percentage'] for item in data}
  
  names = percentages_dict.keys()
  values = percentages_dict.values()
  
  return names, values



