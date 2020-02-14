import workdb

db = 'institute.db'
head = ('ФИО','ФАКУЛЬТЕТ','ГРУППА','Студенческий','ОЦЕНКИ')

def excellent():
	with workdb.Dbconn(db) as conn:
		conn.execute("SELECT Name, Faculty, Groups, Document FROM \
			(SELECT students.name as Name, faculty.title as Faculty, groups.title as Groups, students.student_document as Document, AVG(marks.mark) as AVG_Marks \
	         FROM students INNER JOIN groups ON students.group_id = groups.id INNER JOIN faculty ON groups.faculty_id = faculty.id \
	         INNER JOIN marks ON students.id = marks.students_id GROUP BY name) WHERE AVG_Marks=5")
		print('\nСписок отличников:')
		print('-'*60)
		print(f'{head[0]:20} {head[1]:10} {head[2]:10} {head[3]:20}')
		print('-'*60)
		for i in conn.fetchall():
			print(f'{i[0]:20} {i[1]:10} {i[2]:10} {i[3]:20}')

def all_info():
	with workdb.Dbconn(db) as conn:
		conn.execute("SELECT students.name as Name, faculty.title as Faculty, groups.title as Groups, students.student_document as Document  \
	                  FROM students \
	                  INNER JOIN groups ON students.group_id = groups.id \
	                  INNER JOIN faculty ON groups.faculty_id = faculty.id \
	                  ORDER BY Name")
		print('\nИнформация о студентах:')
		print('-'*60)
		print(f'{head[0]:20} {head[1]:10} {head[2]:10} {head[3]:15}')
		print('-'*60)
		for i in conn.fetchall():
			print(f'{i[0]:20} {i[1]:10} {i[2]:10} {i[3]:15}')

def find_document(document):
	with workdb.Dbconn(db) as conn:
		conn.execute("SELECT * FROM (SELECT students.student_document as Document, students.name as Name, faculty.title as Faculty, groups.title as Groups, GROUP_CONCAT(mark) as Marks \
	                FROM students \
					INNER JOIN groups ON students.group_id = groups.id \
					INNER JOIN faculty ON groups.faculty_id = faculty.id \
					INNER JOIN marks ON students.id = marks.students_id \
					GROUP BY name) WHERE Document=?",(document,))
		print(f'\nИнформация по студенческому {document}: ')
		print('-'*75)
		print(f'{head[3]:15} {head[0]:20} {head[1]:10} {head[2]:10} {head[4]:20}')
		print('-'*75)
		for i in conn.fetchall():
			print(f'{i[0]:15} {i[1]:20} {i[2]:10} {i[3]:10} {i[4]:20}')	

def check_document(in_document):
	with workdb.Dbconn(db, 'w') as conn:
		conn.execute("SELECT * FROM students WHERE student_document=?", (in_document,))
		if conn.fetchall():
			return False
		return True

def check_group(in_faculty, in_group):
    with workdb.Dbconn(db, 'w') as conn:
        conn.execute("SELECT * FROM faculty WHERE title=?",(in_faculty, ))
        if not conn.fetchall():
            conn.execute("INSERT INTO faculty VALUES (null,?)",(in_faculty, ))
        conn.execute("SELECT * FROM groups WHERE title=?",(in_group, ))
        if not conn.fetchall():
            conn.execute("INSERT INTO groups VALUES (null,?,(SELECT id FROM faculty WHERE title=?))",(in_group, in_faculty))

def input_students(in_name, in_group, in_document):
    with workdb.Dbconn(db, 'w') as conn:
        conn.execute("INSERT INTO students VALUES (null,?,(SELECT id FROM groups WHERE title=?),?)",(in_name, in_group, in_document))

def update_students(in_name, in_group, in_document):
    with workdb.Dbconn(db, 'w') as conn:
        conn.execute("UPDATE students SET name=?,group_id=(SELECT id FROM groups WHERE title=?) WHERE student_document=?",(in_name, in_group, in_document))

def delete_students(in_document):
	with workdb.Dbconn(db, 'w') as conn:
		conn.execute("DELETE FROM marks WHERE students_id=(SELECT id FROM students WHERE student_document=?)", (in_document,))
		conn.execute("DELETE FROM students WHERE student_document=?", (in_document,))
