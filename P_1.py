def add_records(feild:str,reg_no:int,name:str,fathername:str,cgpa:float):
    student_records=feild+","+str(reg_no)+","+name+","+fathername+","+str(cgpa)+"\n"
    file_output=open("student.txt",'a')
    file_output.write(student_records)
    file_output.close()
def display_records():
    file_input=open("student.txt",'r')
    records=file_input.read()
    print(records)
    file_input.close()
def search(registration_number):
    file_input=open("student.txt",'r')
    for line in file_input:
        reg_n=line.split(",")[1]
        if reg_n==registration_number:
            print(line)
            break
    file_input.close()
def update(reg_no,cgpa:int,feild:str):
    file_input=open("student.txt",'r+')
    for line in file_input:    
        record=line.strip().split(",")
        if record[1]==reg_no:
            record[0]=feild
            record[4]=str(cgpa)
            break
    line= record[0] +","+record[1] +","+record[2] +","+record[3] +","+record[4]
    file_input.seek(0)
    file_input.writelines(line)
    file_input.close()
    
    