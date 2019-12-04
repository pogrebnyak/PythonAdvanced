countries_dict = {
    'Украина':'Киев',
    'Россия':'Москва',
    'Германия':'Берлин',
    'Франция':'Париж',
}
countries = ['Украина', 'Чехия', 'Польша', 'Франция']

for country in countries:
    if country in countries_dict:
        print(countries_dict[country])