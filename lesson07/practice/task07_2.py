import config


while True:
    print('1. Администратор')
    print('2. Пользователь')
    print('3. Выход')
    s = input('Сделайте выбор: ')
    if s == '1':
        while True:
            print('\n1.Добавить студента')
            print('2.Изменить информацию о студенте')
            print('3.Удалить студента')
            print('4.Выход')
            s = input('Сделайте выбор: ')
            if s == '1':
                in_document = input('Введите номер студенческого: ')
                if config.check_document(in_document):
               	   in_name = input('Введите ФИО студента: ')
               	   in_faculty = input('Введите название факультета: ')
               	   in_group = input('Введите номер группы: ')
                   config.check_group(in_faculty, in_group)
                   config.input_students(in_name,  in_group, in_document)
                   print(f'Студент добавлен: {in_document} {in_name} {in_group} {in_faculty}')
                else:
               	   print('Такой студенческий уже есть!')
            if s == '2':
                in_document = input('Введите номер студенческого: ')
                if not config.check_document(in_document):
               	   in_name = input('Введите ФИО студента: ')
               	   in_faculty = input('Введите название факультета: ')
               	   in_group = input('Введите номер группы: ')
                   config.check_group(in_faculty, in_group)
                   config.update_students(in_name,  in_group, in_document)
                   print(f'Студент обновлен: {in_document} {in_name} {in_group} {in_faculty}')
                else:
               	   print('Такого студенческого нет')
            if s == '3':
               in_document = input('Введите номер студенческого: ')
               if not config.check_document(in_document):	
                   config.delete_students(in_document)
                   print(f'Удален студент со студенческим {in_document}')
               else:
                   print('Такого студенческого нет')
            if s == '4':
               break        	
    if s == '2':
        while True:
            print('\n1.Список отличников')
            print('2.Список студентов')
            print('3.Поиск студента по студенческому')
            print('4.Выход')
            s = input('Сделайте выбор: ')
            if s == '1':
               config.excellent()
            if s == '2':
               config.all_info()
            if s == '3':
               in_document = input('Введите номер студенческого: ')
               print(in_document)
               if not config.check_document(in_document):	
                   config.find_document(in_document)
               else:
                   print('Такого студенческого нет')
            if s == '4':
               break
    if s == '3': 
        break