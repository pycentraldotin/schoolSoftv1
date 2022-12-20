import student

# load data from file into memory
students = student.load_student_info()
while True:
    print("Welcome to School Management Software v01")
    print("1. Display Student Details")
    print("2. Update Student's Total Marks and Grade")
    print("3. Enter Student Details")
    print("e. Exit")
    x = input("Please select: ")

    if x == '1':
        for s in students:
            print(s['name'],s['dob'],s['grade'],s['total_marks'])
    elif x == '2':
        for s in students:
            s['total_marks'] = student.calc_total_marks(s)
            s['grade'] = student.calc_grade(s)
    elif x == '3':
        s = student.enter_student_details()
        # newly entered student dictionary is added to the 'students' list
        students.append(s)
    elif x == 'e':
        break
