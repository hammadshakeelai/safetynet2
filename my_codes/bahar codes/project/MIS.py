'''MIS == Management Information System (MIS) in Python.'''
def read_(filename):
    try:
        with open(filename) as input_file:
            return input_file.read()
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def append_(filename, data):
    try:
        with open(filename, 'a') as output_file:
            output_file.write(data + '\n')
            print(f"{data} appended to {filename}.")
    except Exception as e:
        print(f"An error occurred",e)
def remove_(filename, data):
    try:
        with open(filename, 'r') as input_file:###########
            lines = input_file.readlines()################
        with open(filename, 'w') as output_file:
            for line in lines:
                if line.strip().split(',')[0] != data:
                    output_file.write(line)
        print(f"{data} removed from {filename}.")
    except Exception as e:
        print(f"An error occurred",e)
def update_(filename, data):
    try:
        with open(filename, 'r') as input_file:
            lines = input_file.readlines()
        with open(filename, 'w') as output_file:
            for line in lines:
                if line.strip().split(',')[0] != data[0]:
                    output_file.write(line)
                else:
                    output_file.write(data + '\n')
        print(f"{data} update in {filename}.")
    except Exception as e:
        print(f"An error occurred",e)   
def display_student(id):
    students=read_('students_file.txt')
    for student in students:
        if student.strip().split(',')[0]==id:
            print(student)
def display_student_courses(id):
    courses=read_('student_courses_file.txt')
    for course in courses:
        if course.strip().split(',')[0]==id:
            print(course)
def display_cgpa(id):
    students=read_('students_file.txt')
    for student in students:
        if student.strip().split(',')[0]==id:
            print(student[-1])
def main():
    while True:
        level=input("Are you a {0}student {1}faculty,{3}to exit: ")
        if level=='0':
            id=input("enter your id: ")
            password=input("Enter your password: ")
            student_main()
        elif level=='1':
            password=input("Enter faculty password: ")
            if password==read_('password_ENV_file.txt'):
                print('password accepted')
            else:
                while password!=read_('password_ENV_file.txt'):
                    print("wrong password, try again")
                    password=input("Enter faculty password: ")
            faculty_main()
        elif level=='3':
            print('Exiting...')
            break
        else:
            print("###########\nInvalid input\n###########")
def display_students():
    print(read_('students_file.txt'))
def display_teachers():
    print(read_('teachers_file.txt'))
def display_department():
    print(read_('departments_file.txt'))
def display_faculties():
    print(read_('faculties_file.txt'))
def display_courses():
    print(read_('courses_file.txt'))


def student_main():
    print("\nUniversity Management System")
    print("1. Display Student")
    print("2. Display student Courses")
    print("3. Display cGPA")
    print("4. Display Attendance")
    print("5. Exit")
    choice=input('Enter your choice: ')
    if choice=='1':
        id = input('Enter your student ID: '  )
        display_student(id)
    elif choice=='2':
        id = input('Enter your student ID: '  )
        display_student_courses(id)
    elif choice=='3':
        id = input('Enter your student ID: '  )
        display_cgpa(id)
    elif choice=='4':
        print('Attendance not available')
        print("net nai hai")
    elif choice=='5':
        print('Exiting...')
        return
def faculty_main():
    print('1. Add Course')
    print('2. Add Student')
    print('3. Add department')
    print('4. Add teacher')
    print('5. Add faculty')
    
    print('6. Remove Course')
    print('7. Remove Student')
    print('8. Remove department')
    print('9. Remove teacher')
    print('10. Remove faculty')
    
    print('11. Update Course')
    print('12. Update Student')
    print('13. Update department')
    print('14. Update teacher')
    print('15. Update faculty')
    
    print('16. Display all courses')
    print('17. Display all students')
    print('18. Display all departments')
    print('19. Display all teachers')
    print('20. Display all faculties')
    
    print('21. Add Student courses')
    print('22. Update Student courses')
    print('23. Display Student courses')
    print("24. Remove Student courses")
    
    print('25. Exit')
    choice=input('Enter your choice: ')
    if choice=='1':
        name=input('Enter name of course: ')
        id=input('Enter name of id: ')
        code=input('Enter name of code: ')
        course_manager=input('Enter name of course manager: ')
        course_data=id+','+name+','+code+','+course_manager
        append_('courses_file.txt',course_data)
    elif choice=='2':
        name=input('Enter name of student: ')
        fname=input('Enter name of students father: ')
        department=input('Enter name of students department: ')
        age=input('Enter age of students: ')
        id=input("Enter id of student: ")
        cgpa=input("Enter the previous cgpa of student: ")
        student_data=id+","+name+','+fname+','+department+','+age+','+cgpa
        append_('students_file.txt',student_data)
    elif choice=='3':
        name=input('Enter name of department: ')
        building=input('Enter the building of this department: ')
        program=input('Enter the programs of this department: ')
        id=input("Enter id of this department: ")
        department_data= id+','+building+','+program+','+name
        append_('departments_file.txt',department_data)
    elif choice=='4':
        name=input('Enter name of teacher: ')
        fname=input('Enter name of teachers father: ')
        department=input('Enter name of teachers department: ')        
        id=input("Enter id of teacher: ")
        age=input('Enter age of teachers: ')
        t_score=input("Enter teachers teaching score: ")
        teacher_data=id+','+name+','+fname+','+department+","+age+','+t_score
        append_('teachers_file.txt',teacher_data)
    elif choice=='5':
        name=input('Enter name of faculty: ')
        fname=input('Enter name of faculties father: ')
        job=input('Enter name of job: ')        
        building=input('Enter name of building: ')        
        id=input("Enter id of faculty: ")
        age=input('Enter age of faculties: ')
        faculty_data=id+','+name+','+fname+','+job+','+building+','+age
        append_('faculties_file.txt',faculty_data)    
    elif choice=='6':
        id=input('Enter id of course: ')
        remove_('courses_file.txt',id)
    elif choice=='7':
        id=input('Enter id of student: ')
        remove_('students_file.txt',id)
    elif choice=='8':
        id=input('Enter id of department: ')
        remove_('departments_file.txt',id)
    elif choice=='9':
        id=input('Enter id of teacher: ')
        remove_('teachers_file.txt',id)
    elif choice=='10':
        id=input('Enter id of faculty: ')
        remove_('faculties_file.txt',id)
    elif choice=='11':
        id=input('Enter id of course: ')
        name=input('Enter new name of course: ')
        code=input('Enter new code of course: ')
        course_manager=input('Enter new course manager: ')
        data=id+','+name+','+code+','+course_manager
        update_('courses_file.txt',data)
    elif choice=='12':
        id=input('Enter id of student: ')
        name=input('Enter new name of student: ')
        fname=input('Enter new name of students father: ')
        department=input('Enter new name of students department: ')
        age=input('Enter new age of students: ')
        cgpa=input("Enter new cgpa of student: ")
        data=id+','+name+','+fname+','+department+','+age+','+cgpa
        update_('students_file.txt',data)
    elif choice=='13':
        id=input('Enter id of department: ')
        building=input('Enter new building of this department: ')
        program=input('Enter new programs of this department: ')
        data=id+','+building+','+program+','+department
        update_('departments_file.txt',data)
    elif choice=='14':
        id=input('Enter id of teacher: ')
        name=input('Enter new name of teacher: ')
        fname=input('Enter new name of teachers father: ')
        department=input('Enter new name of teachers department: ')
        age=input('Enter new age of teachers: ')
        t_score=input("Enter new teachers teaching score: ")
        data=id+','+name+','+fname+','+department+','+age+','+t_score
        update_('teachers_file.txt',data)
    elif choice=='15':
        id=input('Enter id of faculty: ')
        name=input('Enter new name of faculty: ')
        fname=input('Enter new name of faculties father: ')
        job=input('Enter new job of faculties: ')
        building=input('Enter new building of faculties: ')
        age=input('Enter new age of faculties: ')
        data=id+','+name+','+fname+','+job+','+building+','+age
        update_('faculties_file.txt',data)
    elif choice=='16':
        display_courses()
    elif choice=='17':
        display_students()
    elif choice=='18':
        display_department()
    elif choice=='19':
        display_teachers()
    elif choice=='20':
        display_faculties()
    elif choice=='21':
        id=input('Enter id of student: ')
        course=input('Enter name of courses: ')
        data=id+','+course
        append_('student_courses_file.txt',data)
    elif choice=='22':
        id=input('Enter id of student: ')
        course=input('Enter name of courses: ')
        update_('student_courses_file.txt',id+','+course)
    elif choice=='23':
        id=input('Enter id of student: ')
        display_student_courses(id)
    elif choice=='24':
        id=input('Enter id of student: ')
        course=input('Enter name of courses: ')
        remove_('student_courses_file.txt',id+','+course)
    elif choice=='25':
        print('Exiting...')
        return    

main()