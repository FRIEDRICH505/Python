cities = {
'city1': {
'country': 'usa',
'population': '50 million',
'fact': 'born in the USA',
},
'city2': {
'country': 'australia',
'population': '30 million',
'fact': 'wallabies',
'city3': {
'country': 'new zealand',
'population': '35 million',
'fact': 'rugby crazy',
},
}
}
for city, city_info in cities.items():
    print(f"\ncities: {city}")
    full_name = f"{city_info['country']}"
    location = city_info['population']
    fact = city_info['fact']
    print(f"\tcountry: {full_name.title()}")
    print(f"\tpopulation: {location.title()}")
    print(f"\tfact: {fact.title()}")
