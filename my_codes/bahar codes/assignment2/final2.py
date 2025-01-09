def add_student_record(registration_no:int,name:str,fathername:str,cgpa:float):
    try:
        student_records=str(registration_no)+", "+name+", "+fathername+", "+str(cgpa)+"\n"
        file_output=open("student.txt",'a')
        file_output.write(student_records)
    except ValueError:
        print("invalid inputs")
    except Exception as e:
        print(f"an error occured: {e}")
    finally:
        file_output.close() 
def display_all_student_records():
    try:
        file_input=open("student.txt",'r')
        records=file_input.readlines()
        print(records)
    except FileNotFoundError:
        print("file not found")
    except ValueError:
        print(" invalid inputs")
    except Exception as e :
        print( f"an error occured: {e}")
    finally:
        file_input.close()      
def search_student_record(registration_number:int):
    try:
        found=False
        file_input=open("student.txt",'r')
        for line in file_input:
            reg_num=line.split(", ")[0]
            if reg_num==str(registration_number):
                found=True
                print(line.strip())
                break
        if not found:
            print("student not found")
    except FileNotFoundError:
        print("file not found")
    except ValueError:
        print("invalid input")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file_input.close()#/
def update_student_record(reg_no: int, cgpa: float):
    try:
        if cgpa>4 or cgpa<0:
            return "cgpa\'s input is wrong "
        cgpa = f"{round(cgpa, 2):.2f}"   
        updated=False
        file_input=open("student.txt",'r+')
        pointerp=file_input.tell()
        line=file_input.readline()
        while line:
            record=line.strip().split(", ")
            if int(record[0])==reg_no:
                record[3]=cgpa
                updated = True
                break
            
            pointerp=file_input.tell()
            line=file_input.readline()
        line= ", ".join(record) + "\n"
        file_input.seek(pointerp)
        file_input.writelines(line)
        
        if not updated:
            print("Record not found for the given registration number.")
    except FileNotFoundError:
        print("file not found")
    except ValueError as e2:
        print(f"Error in data processing: {e2}")
    except Exception as e:
        print("an error occured: ", e)
    finally:
        file_input.close()
def delete_student_record(reg_no: int):
    try:
        course_list=["cs50","ict0t","pf60lab","cs60","ict1t","pf50lab"]
        for course in course_list:
            delete_studentcourse_record(reg_no,course)
        deleted=False
        file_input=open("student.txt",'r+')
        pointerp=file_input.tell()
        line=file_input.readline()
        while line:
            
            if int(line.strip().split(", ")[0])==reg_no:
                 
                deleted = True
                break
            pointerp=file_input.tell()
            line=file_input.readline()
            
        file_input.seek(pointerp)
        file_input.writelines("0, "+"deleted"+" "*(len(line)-10))
        
        if not deleted:
            print("Record not found for the given registration number.")
        else:
            print("deleted successfully")
    except FileNotFoundError:
        print("file not found")
    except ValueError as e2:
        print(f"Error in data processing: {e2}")
    except Exception as e:
        print("an error occured: ", e)
    finally:
        file_input.close()
def add_student_course(registration_number:int,Course_Code:str,Course_Name:str,Percentage:int,Grade:str):
    try:
        file_output=open("course.txt","a")
        course1=str(registration_number)+", "+Course_Code+", "+Course_Name+", "+str(Percentage)+", "+Grade+"\n"
        file_output.write(course1)
        print("course added")
    except FileNotFoundError:
        print("file not found")
    except ValueError:
        print("input error")
    except Exception as e:
        print(" an error occured : ",e)
    finally:
        file_output.close()
def display_student_courses(registration_number:int):
    try:
        file_input=open("course.txt","r")
        lines=file_input.readlines()
        for line in lines:
            if line.strip().split(", ")[0]==str(registration_number):
                print(line.strip())
    except ValueError:
        print("invalid inputs")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured ",e)
    finally:
        file_input.close()
def search_student_course(registration_number:int,Course_Code:str):
    try:
        file_input=open("course.txt","r")
        lines=file_input.readlines()
        for line in lines:
            if line.strip().split(", ")[0]==str(registration_number) and line.strip().split(", ")[1]==Course_Code:
                print(line.strip())
                break
    except ValueError:
        print("invalid inputs")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured ",e)
    finally:
        file_input.close()
def modify_studentcourse_record(registration_number:int,Course_Code:str,percentage:float,grade:str):
    try:
        found=False
        file_input=open("course.txt","r+")
        lines=file_input.readlines()
        for line in lines:
            size=len(line)
            course_record=line.strip().split(", ")
            if course_record[0]==str(registration_number) and course_record[1]==Course_Code:
                course_record[3]=f"{percentage:.2f}"
                course_record[4]=grade
                found=True
                break
        if found: 
            newline=", ".join(course_record)
            file_input.seek(file_input.tell()-size-1)  
            file_input.write(newline+"\n") 
        else:
            print("course of student not found")    
    except ValueError:
        print("invalid inputs")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured ",e)
    finally:
        file_input.close()  
def delete_studentcourse_record(registration_number:int,Course_Code:str):
    try:
        found=False
        file_input=open("course.txt","r+")
        lines=file_input.readlines()
        for line in lines:
            size=len(line)
            course_record=line.strip().split(", ")
            if course_record[0]==str(registration_number) and course_record[1]==Course_Code:
                found=True
                break
        if found: 
            newline=", ".join(course_record)
            file_input.seek(file_input.tell()-size-1)  
            file_input.write("0, deleted"+" "*(size-11)+"\n") 
        else:
            print("course of student not found")    
    except ValueError:
        print("invalid inputs")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occured ",e)
    finally:
        file_input.close()  
def main():
    print("\n1. Add student record")
    print("2. Display all student records")
    print("3. Search student record by registration number")
    print("4. Update student record by registration number")
    print("5. Delete student record by registration number")
    print("6. Add course record for a student")
    print("7. Display all course records for a student")
    print("8. Search course record for a student by course code")
    print("9. Modify course record for a student")
    print("10. Delete course record for a student by course code")
    print("11. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        try:
            registration_no=int(input("Enter registration number: "))
            name=input("Enter name: ")
            fathername=input("Enter father name: ")
            cgpa=float(input("Enter cgpa: "))
            add_student_record(registration_no,name,fathername,cgpa)
        except FloatingPointError as e:
            print
        except Exception as e:
            print('no input given')
        
    elif choice==2:
        display_all_student_records()
    elif choice==3:
        registration_number=int(input("Enter registration number: "))
        search_student_record(registration_number)
    elif choice==4:
        reg_no=int(input("Enter registration number: "))
        cgpa=float(input("Enter new cgpa: "))
        update_student_record(reg_no,cgpa)
    elif choice==5:
        reg_no=int(input("Enter registration number: "))
        delete_student_record(reg_no)
    elif choice==6:
        registration_number=int(input("Enter registration number: "))
        course_code=input("Enter course code: ")
        course_name=input("Enter course name: ")
        percentage=float(input("Enter course percentage: "))
        grade=input("Enter course grade: ")
        add_student_course(registration_number,course_code,course_name,percentage,grade)
    elif choice==7:
        registration_number=int(input("Enter registration number: "))
        display_student_courses(registration_number)
    elif choice==8:
        registration_number=int(input("Enter registration number: "))
        course_code=input("Enter course code: ")
        search_student_course(registration_number,course_code)
    elif choice==9:
        reg_no=int(input("Enter registration number: "))
        course_code=input("Enter course code: ")
        percentage=float(input("Enter new course percentage: "))
        grade=input("Enter new course grade: ")
        modify_studentcourse_record(reg_no,course_code,percentage,grade)
    elif choice==10:
        reg_no=int(input("Enter registration number: "))
        course_code=input("Enter course code: ")
        delete_studentcourse_record(reg_no,course_code)
    elif choice==11:
        print("Exiting...")
        return
if __name__=="__main__":
    main()