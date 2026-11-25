from backbone import Person,Student, Teacher

user1 = Person(name='kc',
               surname='lb',
               age=12,
               identity=19732698)
user1 = Student(student_number="kc",
                course_name='EMC',
                mark={
                 "80–100": "A",
                 "70–79" : "B",
                 "60–69" : "C",
                 "50–59" : "D",
                 "0–49"  : "F"
                },
                enrollment_statues=4,
                surname='lb',
                identity=19732698,
                age=12,
                name='kc',
                )
print(f"\n{'Mark':<6} | {'Grade':<10}")
print("-" * 25)
for new_mark,grade in user1.mark.items():
    print(f'{new_mark} | {grade}')


user2 = Teacher(
    name="casey",
    surname="lubese",
    age=20,
    identity=260684430,
    employee_id=21056,
    subject_taught="Mathematics",
    monthly_salary=50000,
    student_assigned=[],

)

user2.add_students("Casey")
user2.add_students("lubese")
user2.add_students("Khumalo")

user2.remove_student()
print(f"\nStudent(s) enrolled: ")
print(user2.student_assigned)
