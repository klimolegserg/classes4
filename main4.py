class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        #средняя оценка студентам за ДЗ
    def midgrade_st(self):
        values_st = self.grades.values()
        values_list = list(values_st)
        average = sum(values_list)/len(values_list)
        return average
      
    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашнее задание: {self.average()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return self == other
    
    def __it__(self, other):
        return self < other
    
    def __gt__(self, other):
        return self > other  

    def rate_lec(self, lecturer, course, grade): # функция выставления оценок лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
           
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

        # Средная оценка лекторам 
    def midgrade_lc(self):
        values_st = self.grades.values()
        values_list = list(values_st)
        average = sum(values_list)/len(values_list)
        return average

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average()}'
    
    def __eq__(self, other):
        return self == other
    
    def __it__(self, other):
        return self < other
    
    def __gt__(self, other):
        return self > other
  

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade): # функция выствления оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
    
#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

student1 = Student('Bob', 'Marley', 'male') # создание экземпляров студентов
student2 = Student('Robert', 'McFerrin', 'male')

student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

list_student = [student1, student2]
list_st_course = ['Python']

# средняя оценка за ДЗ по всем студентам курса
def mid_stud_course_grade(list_student, list_st_course):
    for course in list_st_course:
        for student in list_student:

            # ?????

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

mentor1 = Mentor('Ozzy', 'Osbourne') # создание экземпляров менторов
mentor2 = Mentor('Tommy', 'Iommi')

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

lecturer1 = Lecturer('Adrian', 'Smith') # создание экземпляров лекторов
lecturer2 = Lecturer('Dave', 'Murray')

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

list_lecture = [lecturer1, lecturer2]
list_lc_course = ['Python']

# средняя оценка за лекции у лекторов на курсе
def mid_lc_course_grade(list_lecture, list_lc_course):
    for course in list_lc_course:
        for student in list_student:

            # ??????

reviewer1 = Reviewer('Steve', 'Harris') # создание экземпляров проверяющих
reviewer2 = Reviewer('Clive', 'Burr')

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 9) # выставление оценок студентам
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 6)

student1.rate_lec(lecturer1, 'Python', 10) # выствление оценок лекторам
student1.rate_lec(lecturer2, 'Python', 10)
student2.rate_lec(lecturer1, 'Python', 9)
student2.rate_lec(lecturer2, 'Python', 8)

#print(best_student.grades)

