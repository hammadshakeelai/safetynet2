# Given a text file employees.txt with data in the format given belowAlice, Active
# Bob, Inactive
# James Smith, Inactive
# Michael Smith, Active
# Write a Python program to:
# 1. Take the employee's name and status (activate or deactivate) as input.
# 2. Check if the name exists in the file:
# If not, display "Employee not found."
# 3. If the name exists:
# For activation, update to "Active" unless it's already active.
# For deactivation, update to "Inactive" unless it's already inactive.
#to update
final_ouput_data=''
#inputs
name=input("enter your name (like 'Firstname Lastname' ) : ")
status_input=input("enter status '0 for activate' , '1 for deactivate' : ")
#to activate or deactivate ,easier to test
flag=0
if status_input=="0":
    status="Active"
else:
    status="Inactive"
#open
file_input = open("employee.txt", 'r')
#readline
line = file_input.readline()

while(line):#if line not empty continue
    
    #store full name into variable
    name_in_list=""
    status_in_list=""
    name_to_status_flag=1
    line=line.strip()
    for i in range(len(line)):
        if line[i]==",":
            name_to_status_flag=0
            continue
        if name_to_status_flag:
            name_in_list=name_in_list+line[i]
        else:
            status_in_list=status_in_list+line[i]
            
    name_in_list = name_in_list.strip()
    status_in_list = status_in_list.strip()
    #if strored name == input # change flag and perform activation or deactivation 
    if name.strip() == name_in_list:
        if status_in_list.lower() != status.lower():
            line=name+", " +status
        else:
            print(f"The status is already '{status}'.")
        flag=1
        
    final_ouput_data=final_ouput_data+line+"\n"
    line = file_input.readline()
    
file_input.close()

file_output = open("employee.txt", 'w')
file_output.writelines(final_ouput_data)
file_output.close()
    
if not flag:
    print("Employee not found.")