def display_records():
    file_input=open("student.txt",'r')
    records=file_input.read()
    print(records)
    file_input.close()
display_records()
def delete(registration_number):
    file_ouput=open('student.txt','r+')
    line=file_ouput.readline()
    while line!='':
        size=len(line)
        records=line.split(",")
        if records[1]==str(registration_number):
            file_ouput.writelines("p"*size)
            break
        line=file_ouput.readline()
    file_ouput.close()
delete(0)
print()
display_records()
