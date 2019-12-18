from abc import ABC, abstractmethod
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta


class Person(ABC):

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def age(self):
        today = datetime.now().date()
        date_of_birth_obj = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
        age_person = relativedelta(today, date_of_birth_obj).years
        return age_person


class Enrollee(Person):

    def __init__(self, name, date_of_birth, faculty):
        super().__init__(name, date_of_birth)
        self.faculty = faculty

    def info(self):
        return (f'Фамилия       : {self.name}\n'
                f'Дата рождения : {self.date_of_birth}\n'
                f'Факультет     : {self.faculty}')

    def age(self):
        today = datetime.now().date()
        date_of_birth_obj = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
        age_enrollee = relativedelta(today, date_of_birth_obj).years
        return age_enrollee

    def __str__(self):
        return f'{self.name:15}{self.date_of_birth:11}{self.faculty:6}'


class Student(Person):

    def __init__(self, name, date_of_birth, faculty, course):
        super().__init__(name, date_of_birth)
        self.faculty = faculty
        self.course = course

    def info(self):
        return (f'Фамилия       : {self.name}\n'
                f'Дата рождения : {self.date_of_birth}\n'
                f'Факультет     : {self.faculty}\n'
                f'Курс          : {self.course}')

    def age(self):
        today = datetime.now().date()
        date_of_birth_obj = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
        age_student = relativedelta(today, date_of_birth_obj).years
        return age_student

    def __str__(self):
        return f'{self.name:15}{self.date_of_birth:11}{self.faculty:6}{self.course:3}'


class Teacher(Person):

    def __init__(self, name, date_of_birth, faculty, position, experience):
        super().__init__(name, date_of_birth)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def info(self):
        return (f'Фамилия       : {self.name}\n'
                f'Дата рождения : {self.date_of_birth}\n'
                f'Факультет     : {self.faculty}\n'
                f'Должность     : {self.position}\n'
                f'Стаж          : {self.experience}')

    def age(self):
        today = datetime.now().date()
        date_of_birth_obj = datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()
        age_teacher = relativedelta(today, date_of_birth_obj).years
        return age_teacher

    def __str__(self):
        return f'{self.name:15}{self.date_of_birth:11}{self.faculty:6}{self.position:20}{self.experience:7}'


def print_age_range(persons, age_low, age_high):
    print(f'Вывод персон чей возраст от {age_low} до {age_high}:')
    for person in persons:
        if (person.age()) >= age_low and (person.age()) <= age_high:
            print(f'{person}  {person.age()} лет')
    print()


def print_all_str(persons):
    print(f'Вывод всей информации из базы:')
    for person in persons:
        print(person)
    print()

persons_all = []

student = Student('Иванов', '2000-02-14', 'ФИВТ', '2 курс')
persons_all.append(student)
print(student.age())
student2 = Student('Петров', '2001-03-28', 'АСУ', '3 курс')
persons_all.append(student2)
print(student2.age())
teacher = Teacher('Дорошенко', '1985-06-13', 'ФИВТ', 'Преподаватель', '5 лет')
persons_all.append(teacher)
print(teacher.age())
enrollee = Enrollee('Тимошенко', '2003-07-30', 'ИНН')
persons_all.append(enrollee)
print(enrollee.age())
print(teacher.info())
print()


print_all_str(persons_all)
print_age_range(persons_all, 18, 20)

