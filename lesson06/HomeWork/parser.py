# coding: utf-8
from bs4 import BeautifulSoup
import requests


while True:
    print('-' * 55)
    print('Програма з виведенням прогнозу погоди в заданій локації')
    city = input('Введіть місто: ')
    if city == '':
        city = 'Київ'

    resp = requests.get(
        f'https://ua.sinoptik.ua/погода-{city}/10-днів')

    soup = BeautifulSoup(resp.text, 'lxml')

    if soup.find("body", class_="ua p404"):
        print('На жаль, інформація, яку ви шукали, в даний момент на сайті відсутня.')
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
        while True:
            input_date = input(f'Введіть дату з {date_list[0]} по {date_list[len(date_list) - 1]} : ')
            if input_date not in date_list:
                for i in date_dict.values():
                    print(i)
                break
            else:
                print(date_dict[input_date])
            if input('Показати іншу дату (т/н)') != 'т':
                break
            
    if input('Продовжити пошук (т/н)') != 'т':
        break
