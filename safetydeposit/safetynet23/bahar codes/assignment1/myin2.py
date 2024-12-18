name: str=input("enter name:  ")
age:int =int(input("enter age:  "))
program:str=input("enter program name:  ")
if program=="AI":
    subject1="pf"
    subject2="ict"
    subject3="math"
    subject4="lab"
else:
    subject1="b.st"
    subject2="eco"
    subject3="acc"
    subject4="fin"    
file_ouput=open("name_age_program.txt","a")
file_ouput.write(name + '\n')
file_ouput.write(str(age) + '\n')
file_ouput.write(program + '\n')
file_ouput.close()
file_ouput=open("name_subjects.txt","a")
file_ouput.write(f"{name}, {subject1}, {subject2}, {subject3}, {subject4}\n")
file_ouput.close()
