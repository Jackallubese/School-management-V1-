class Person:

    def __init__(self, name, surname, age, identity):
        self.name = name
        self.surname = surname
        self.fullname = name+' '+ surname
        self.age = age
        self.identity = identity
        self.email = "{}{}@gmail.com".format(name, surname)

    def intro(self):
        detail = self.fullname
        age = self.age
        print(f"Hello, I am {detail.title()} and i am {age} years old")


class Student(Person):

    def __init__(self,name, surname, age, identity, student_number, course_name, mark, enrollment_statues):
        super().__init__(name, surname, age, identity)

        self.student_number = student_number
        self.course_name = course_name
        self.mark = mark
        self.enrollment_statues = enrollment_statues

    def add_mark(self, new_mark):
        self.mark.append(new_mark)


class Teacher(Person):

    def __init__(self, name, surname, age, identity, employee_id, subject_taught, monthly_salary, student_assigned):
        super().__init__(name, surname, age, identity,)
        self.name = name
        self.surname = surname
        self.fullname = "{} {}".format(name, surname)
        self.age = age
        self.identity = identity
        self.employee_id = employee_id
        self.subject_taught = subject_taught
        self.monthly_salary = monthly_salary
        self.student_assigned = student_assigned

    def add_students(self, new_student):
        self.new_student = new_student
        self.student_assigned.append(new_student)

    def remove_student(self):
        checked_out = []
        student_removed = self.student_assigned.pop()

        checked_out.append(student_removed)
        print(f"\nStudent(s) excluded: ")
        print(checked_out)

