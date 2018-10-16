# name, course, etc are classes here
# Self refers to the objects (Here student1, student2, etc)


class Student:

    def __init__(self, name, course, grades, good_behaviour):
        self.name = name
        self.course = course
        self.grades = grades
        self.good_behaviour = good_behaviour


student1 = Student("Nik", "Business", 7, True)
student2 = Student("Sam", "Btech", 6, False)
student3 = Student("Shiv", "", 9, True)

print(student1.name)
print(student3.good_behaviour)
print(student3.course)
print(student2.grades)
