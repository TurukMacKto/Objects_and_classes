class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def aver_grades(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        return round((sum(map(sum, self.grades.values())) / grades_count), 1)

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Student):
            raise TypeError("Operand should be Student ")

        return other if isinstance(other, float) else other.aver_grades()

    def __eq__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() == ag

    def __lt__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() < ag

    def __le__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() <= ag

    def __str__(self):

        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade for hw: " \
               f"{self.aver_grades()}" \
               f"\nCourses in progress: {', '.join(self.courses_in_progress)}" \
               f"\nCompleted courses: {', '.join(self.finished_courses)}"

    def rate_lectur(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = []
                lecturer.grades[course].append(grade)
        else:
            return 'Mistake'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_grades(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        return round((sum(map(sum, self.grades.values())) / grades_count), 1)

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Operand should be Lecturer ")

        return other if isinstance(other, float) else other.aver_grades()

    def __eq__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() == ag

    def __lt__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() < ag

    def __le__(self, other):
        ag = self.verify_data(other)
        return self.aver_grades() <= ag

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.aver_grades()}"


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = []
                student.grades[course].append(grade)
        else:
            return 'Mistake'

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}"


student1 = Student('Roy', 'Eman', 'mail')
student1.courses_in_progress += ['Python', 'Git', 'Django']
student1.finished_courses += ['Introduction to programming']

student2 = Student(' Hermione', 'Granger', 'femail')
student2.courses_in_progress += ['Python', 'Django']
student2.finished_courses += ['Introduction to programming', 'Git']

student3 = Student('Harry', 'Potter', 'mail')
student3.courses_in_progress += ['Python', 'Git']
student3.finished_courses += ['Introduction to programming', 'Django']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Jim', 'Beam')
reviewer2.courses_attached += ['Git', 'Django']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Johnny', 'Walker')
lecturer2.courses_attached += ['Python', 'Django']

reviewer1.rate_hw(student1, 'Python', 9), reviewer1.rate_hw(student1, 'Python', 8)

reviewer1.rate_hw(student2, 'Python', 9), reviewer1.rate_hw(student2, 'Python', 8)

reviewer1.rate_hw(student3, 'Python', 8), reviewer1.rate_hw(student3, 'Python', 9)

reviewer2.rate_hw(student1, 'Git', 9), reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Django', 10), reviewer2.rate_hw(student1, 'Django', 9)

reviewer2.rate_hw(student2, 'Django', 8), reviewer2.rate_hw(student2, 'Django', 8)

reviewer2.rate_hw(student3, 'Git', 7), reviewer2.rate_hw(student3, 'Git', 9)

student1.rate_lectur(lecturer1, 'Python', 8), student1.rate_lectur(lecturer1, 'Git', 9)
student1.rate_lectur(lecturer2, 'Python', 8), student1.rate_lectur(lecturer2, 'Django', 7)

student2.rate_lectur(lecturer1, 'Python', 9), student2.rate_lectur(lecturer1, 'Python', 9),
student2.rate_lectur(lecturer2, 'Python', 7), student2.rate_lectur(lecturer2, 'Django', 8)

student3.rate_lectur(lecturer1, 'Python', 9), student3.rate_lectur(lecturer1, 'Python', 9)
student3.rate_lectur(lecturer2, 'Python', 8), student3.rate_lectur(lecturer2, 'Python', 8)

print()
print("Reviewers:")
print()
print(reviewer1)
print()
print(reviewer2)
print('===================================================')
print()
print("Lecturers:")
print()
print(lecturer1)
print()
print(lecturer2)
print('===================================================')
print()
print("Students:")
print()
print(student1)
print()
print(student2)
print()
print(student3)
print('===================================================')
print(lecturer1 >= lecturer2)
print(lecturer1 < lecturer2)
print(student1 <= student2)
print(student2 == student3)
print(lecturer1 < lecturer2)
print(student1 > student3)
print(student2 <= student1)
print('===================================================')
if lecturer1 > lecturer2:
    print('1st first place of lecturers ranking: ', lecturer1.name, lecturer1.surname,
          '\n2nd first place of lecturers ranking:', lecturer2.name, lecturer2.surname)
if lecturer1 < lecturer2:
    print('1st first place of lecturers ranking: ', lecturer2.name, lecturer2.surname,
          '\n2nd first place of lecturers ranking:', lecturer1.name, lecturer1.surname)
if lecturer1 == lecturer2:
    print(lecturer1.name, lecturer1.surname, 'is equal', lecturer2.name, lecturer2.surname)
print('-------------------------------------------------------------------------------------')
if student1 > student2 and student3:
    print(student1.name, student1.surname, 'is the best student')
if student2 > student1 and student3:
    print(student2.name, student2.surname, 'is the best student')
if student3 > student1 and student2:
    print(student3.name, student3.surname, 'is the best student')


