file = open("employee.txt", 'r+')
print("""Enter 1 to Activate Employee Record\nEnter 2 to Deactivate Employee Record""")
employee_state = input("Enter Your Choice: ")
position = 0
if employee_state == '1' or employee_state == '2':
    if employee_state == '1':
        employee_state = "Active  "
    elif employee_state == '2':
        employee_state = "Inactive"
    
    employee_name = input("Enter Employee Name: ")
    line = file.readline()
    while(line):
        print(line, end="")
        name = line.split(",")[0]
        state = line.split(",")[1]
        if name == employee_name and state != employee_state:
            file.seek(position)
            file.write(employee_name + ", " + employee_state)
            break
        position = file.tell()
        line = file.readline()
        
else:
    print("Wrong Choice.....")