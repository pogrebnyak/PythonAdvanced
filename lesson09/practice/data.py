import random


def random_name():
    result = (random.choice(surname), random.choice(name), random.choice(patronymic))
    result = ' '.join(result)

    return result

curators = (
    'Броваренко Олександр Олександрович',
    'Захарчук Антон Йосипович',
    'Боднаренко Павло Валентинович',
    'Боднаренко Станіслав Анатолійович',
    'Пономарчук Костянтин Романович',
    'Мірошниченко Євген Романович',
    'Кравченко Станіслав Євгенійович',
    'Васильєв Олександр Романович',
    'Сергієнко Валерій Тарасович',
    'Мірошниченко Станіслав Валентинович'
)

name = (
    'Євген',
    'Іван',
    'Ігор',
    'Андрій',
    'Антон',
    'Артем',
    'Болеслав',
    'Вадим',
    'Валентин',
    'Валерій',
    'Василь',
    'Віктор',
    'Данил',
    'Дмитро',
    'Кирил',
    'Костянтин',
    'Лев',
    'Леонід',
    'Максим',
    'Микита',
    'Микола',
    'Мирослав',
    'Олександр',
    'Павло',
    'Роман',
    'Станіслав',
)

patronymic = (
    'Євгенович',
    'Євгенійович',
    'Іванович',
    'Анатолійович',
    'Андрійович',
    'Борисович',
    'Валентинович',
    'Васильович',
    'Володимирович',
    'Йосипович',
    'Миколайович',
    'Михайлович',
    'Олександрович',
    'Олексійович',
    'Романович',
    'Сергійович',
    'Тарасович',
    'Янович',
)

surname = (
    'Іванченко',
    'Антоненко',
    'Боднаренко',
    'Броваренко',
    'Броварчук',
    'Васильєв',
    'Гнатюк',
    'Дмитренко',
    'Захарчук',
    'Кравченко',
    'Кравчук',
    'Крамаренко',
    'Крамарчук',
    'Лисенко',
    'Мірошниченко',
    'Петренко',
    'Пономаренко',
    'Пономарчук',
    'Сергієнко',
    'Середа',
    'Шевчук',
)

faculty = (
    'ЗФ',
    'ІФФ ',
    'ІХФ',
    'ПБФ',
    'РТФ',
    'ТЕФ',
    'ФБМІ',
    'ФБТ',
    'ФЕА',
    'ФЕЛ',
    'ФІОТ',
    'ФЛ ',
    'ФММ',
    'ФСП',
    'ФПМ',
    'ФМФ',
    'ХТФ',
)

groups = (
    '01',
    '02',
    '03'
)