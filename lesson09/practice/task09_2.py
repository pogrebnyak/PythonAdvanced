from mongoengine import *
import task09_1
import data
import random

if __name__ == "__main__":
    connect('db_students')

    for i in range(150):
       name = data.random_name()
       groups = random.choice(data.groups)
       marks = str([(random.randint(2,5)) for x in range(random.randint(2,10))])[1 : -1]
       curator = random.choice(data.curators)
       faculty = random.choice(data.faculty)
       task09_1.Students.create_student(name,groups,marks,curator,faculty)


    task09_1.Students.read_students()
    task09_1.Students.top_marks('ФІОТ')
    task09_1.Students.curator_students('Сергієнко Валерій Тарасович')