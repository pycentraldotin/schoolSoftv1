def calc_total_marks(s):
    """A student dictionary is passed in as input.
    Total marks is calculated from this dictionary and returned."""
    total = sum(s['marks'].values())
    return total


def calc_grade(s):
    """A student dictionary is passed in as input.
    grade is calculated from this dictionary and returned."""
    grade = None
    if s['total_marks'] > 200:
        grade = 'A'
    elif 100 < s['total_marks'] <= 200:
        grade = 'B'
    elif s['total_marks'] <= 100:
        grade = 'C'
    return grade


def load_student_info():
    """Reads data from file and returns list of student dictionaries"""
    student_list = []
    f = open('students_info.csv', 'r')
    for line in f.readlines():
        new_student = {}
        info = line.split(',')
        new_student['name'] = info[0]
        new_student['dob'] = info[1]
        new_student['grade'] = info[2]
        new_student['total_marks'] = info[3]
        new_student['marks'] = {'physics':int(info[4]),'chemistry':int(info[5]),'maths':int(info[6])}
        student_list.append(new_student)
    f.close()
    return student_list


def enter_student_details():
    """Gets student's info from user, writes it to a file and return a student dictionary"""
    name = input("Name: ")
    dob = input("DOB(DD-MMM-YYYY): ")
    marks_physics = input("Physics marks: ")
    marks_chemistry = input("Chemistry marks: ")
    marks_maths = input("Maths marks: ")
    student_info_to_file(name, dob, marks_physics, marks_chemistry, marks_maths)
    new_student = {'name':name,
                   'dob':dob,
                   'marks': {'physics':int(marks_physics), 'chemistry':int(marks_chemistry), 'maths':int(marks_maths)},
                   'total_marks':''}
    return new_student


def student_info_to_file(name, dob, marks_physics, marks_chemistry, marks_maths):
    string_to_write = name+','+dob+','+''+','+''+','+marks_physics+','+marks_chemistry+','+marks_maths+'\n'
    f = open('students_info.csv', 'a')
    f.write(string_to_write)
    f.close()


def student_dict_to_string(s):
    return s['name']+" | "+s['dob']+" | "+str(s['marks']['physics'])+" | "+str(s['marks']['chemistry'])+" | "+str(s['marks']['maths'])