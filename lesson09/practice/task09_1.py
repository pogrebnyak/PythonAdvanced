from mongoengine import *


class Curators(Document):
    name = StringField(unique=True)

class Faculty(Document):
    title = StringField(unique=True)

class Groups(Document):
    title = StringField(unique=True)

class Students(Document):
    name = StringField()
    groups = ReferenceField(Groups)
    marks = ListField()
    curator = ReferenceField(Curators)
    faculty = ReferenceField(Faculty)

    def create_student(in_name,in_group,in_marks,in_curator,in_faculty):
        student_obj = Students.objects(name = in_name)

        if not student_obj:
            if Groups.objects(title=in_group):
                group_obj = Groups.objects.get(title=in_group)
            else:
                group_obj = Groups(title=in_group).save()
            if Curators.objects(name=in_curator):
                curator_obj = Curators.objects.get(name=in_curator)
            else:
                curator_obj = Curators(name=in_curator).save()
            if Faculty.objects(title=in_faculty):
                faculty_obj = Faculty.objects.get(title=in_faculty)
            else:
                faculty_obj = Faculty(title=in_faculty).save()

            student_obj = Students(
                    name = in_name,
                    groups = group_obj,
                    curator = curator_obj,
                    marks = list(map(int,in_marks.split(','))),
                    faculty = faculty_obj).save()

    def delete_students(in_name):
        student_obj = Students.objects(name = in_name)
        student_obj.delete()

    def update_students(in_name,in_group,in_marks,in_curator,in_faculty):
        student_obj = Students.objects(name = in_name)

        if student_obj:
            if Groups.objects(title=in_group):
                group_obj = Groups.objects.get(title=in_group)
            else:
                group_obj = Groups(title=in_group).save()
            if Curators.objects(name=in_curator):
                curator_obj = Curators.objects.get(name=in_curator)
            else:
                curator_obj = Curators(name=in_curator).save()
            if Faculty.objects(title=in_faculty):
                faculty_obj = Faculty.objects.get(title=in_faculty)
            else:
                faculty_obj = Faculty(title=in_faculty).save()

            student_obj.update(
                name = in_name,
                groups = group_obj,
                curator = curator_obj,
                marks = list(map(int,in_marks.split(','))),
                faculty = faculty_obj
            )

    def read_students():
        students = Students.objects()
        for student in students:
            print(f'{student.name:40}|{student.faculty.title:4}|{student.groups.title:^4}|'
                  f'{student.curator.name:^40}|{str(student.marks):^40}|')

    def top_marks(in_faculty):
        students = Students.objects()
        print(f'\nОтличники Факультета {in_faculty}:')
        for student in students:
            if in_faculty == student.faculty.title:
                if (sum(student.marks)/len(student.marks)) >= 5:
                    print(f'{student.name:40}|{student.faculty.title:4}|{student.groups.title:^4}|'
                          f'{student.curator.name:^40}|{str(student.marks):^40}|')

    def curator_students(in_curator):
        students = Students.objects.filter()
        print(f'\nСтуденты куратора {in_curator}:')
        for student in students:
            if in_curator == student.curator.name:
                print(f'{student.name:40}|{student.faculty.title:4}|{student.groups.title:^4}|'
                      f'{student.curator.name:^40}|{str(student.marks):^40}|')





if __name__ == "__main__":
    connect('db_students')










