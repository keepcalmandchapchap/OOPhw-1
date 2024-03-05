class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка' 
    
    def __mid_grade(self):
        list_grades = sum(list(self.grades.values()), [])
        return round(sum(list_grades) / len(list_grades), 1)
        
    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__mid_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'''
    
    def __lt__(self, other):
        return self.__mid_grade() < other.__mid_grade()
    def __le__(self, other):
        return self.__mid_grade() <= other.__mid_grade()
    def __gt__(self, other):
        return self.__mid_grade() > other.__mid_grade()
    def __ge__(self, other):
        return self.__mid_grade() >= other.__mid_grade()
    def __eq__(self, other):
        return self.__mid_grade() == other.__mid_grade()
    def __ne__(self, other):
        return self.__mid_grade() != other.__mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

     
class Lecturer(Mentor):
    def __init__(self, name, surname):
       super().__init__(name, surname)
       self.courses_attached = []
       self.grades_from_students = {}

    def __mid_grade(self):
        list_grades = sum(list(self.grades_from_students.values()), [])
        return round(sum(list_grades) / len(list_grades), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__mid_grade()}'
    
    def __lt__(self, other):
        return self.__mid_grade() < other.__mid_grade()
    def __le__(self, other):
        return self.__mid_grade() <= other.__mid_grade()
    def __gt__(self, other):
        return self.__mid_grade() > other.__mid_grade()
    def __ge__(self, other):
        return self.__mid_grade() >= other.__mid_grade()
    def __eq__(self, other):
        return self.__mid_grade() == other.__mid_grade()
    def __ne__(self, other):
        return self.__mid_grade() != other.__mid_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
    
def students_mid_grade(course, students):
    grades_list = []
    for student in students:
        if course in student.grades:
            grades_list += student.grades[course]
    return round(sum(grades_list) / len(grades_list), 1)

def lecturers_mid_grade(course, lecturers):
    grades_list = []
    for lecturer in lecturers:
        if course in lecturer.grades_from_students:
            grades_list += lecturer.grades_from_students[course]
    return round(sum(grades_list) / len(grades_list), 1)
    

student1 = Student('Jo', 'Barbara', 'male')
student2 = Student('Maria', 'Santa', 'female')
lecturer1 = Lecturer('Chack', 'Palanick')
lecturer2 = Lecturer('Nick', 'Diaz')
reviewer1 = Reviewer('Skot', 'Trimmer')
reviewer2 = Reviewer('Polina', 'Topol')

student1.finished_courses = ['Java']
student1.courses_in_progress = ['Git', 'Python']
student1.grades = {'Git': [7, 9, 6, 10], 'Python': [5, 10, 9, 8]}
print(student1)
print('-' * 10)

student2.finished_courses = []
student2.courses_in_progress = ['Java', 'Python']
student2.grades = {'Java': [7, 4, 8, 5], 'Python': [7, 7, 8, 4]}
print(student2)
print('-' * 10)

print(student1 > student2, student1 < student2, student1 == student2, sep='\n')
print('-' * 10)

lecturer1.courses_attached = ['Git', 'Python']
student1.rate_lect(lecturer1, 'Git', 8)
student2.rate_lect(lecturer1, 'Python', 7)
print(lecturer1)
print('-' * 10)

lecturer2.courses_attached = ['Java']
lecturer2.grades_from_students = {'Java': [10, 8]}
print(lecturer2)
print('-' * 10)

print(lecturer1 > lecturer2, lecturer1 < lecturer2, lecturer1 == lecturer2, sep='\n')
print('-' * 10)

reviewer1.courses_attached = ['Git', 'Java']
print(reviewer1)
print('-' * 10)

reviewer2.courses_attached = ['Python']
reviewer2.rate_hw(student1, 'Python', 3)
print(reviewer2, student1, sep='\n'*2)
print('-' * 10)

all_students = [student1, student2]
all_lecturers = [lecturer1, lecturer2]

print(f'Средняя оценка студентов по курсу "Python" - {students_mid_grade('Python', all_students)}')
print(f'Средняя оценка лекторов по курсу "Git" - {lecturers_mid_grade('Git', all_lecturers)}')

