from bs4 import BeautifulSoup
import requests

city = input('Введите город: ')
# city = 'Киев'

resp = requests.get(
    f'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-{city}/10-%D0%B4%D0%BD%D1%96%D0%B2')

soup = BeautifulSoup(resp.text, 'lxml')

if soup.find("body", class_="ua p404"):
    print('Такого города нет')
else:

    date_list = []
    date_dict = {}
    weather_list = (soup.find("div", class_="tabs").text).split()
    parser_city = (soup.find("div", class_="cityName").text).split()

    for i in range(0, len(weather_list), 7):
        n = weather_list[0 + i:7 + i]
        date_dict[n[1].lstrip('0')] = ' '.join(n)
        date_list.append(n[1].lstrip('0'))

    print(' '.join(parser_city))
    c = input(f'Введите дату c {date_list[0]} по {date_list[len(date_list) - 1]}: ')
    print(date_dict[c])