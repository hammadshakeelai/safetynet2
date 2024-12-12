# The assignment is to perform file operations for maintaining persistent records.
# You will work with two text files (.txt) to (store and manage data related to students) (and their courses).

# {
# Student Fields: Registration Number
# Name
# Father Name
# CGPA
# }
{
Course Fields:
Course Code
Course Name
Percentage
Grade Point
}
# ------------student.txt
# Tasks for a file named student.txt:
-------
# Add Records: Write a function to add student records.('w')
# def add_records(feild:str,reg_no:int,name:str,fathername:str,cgpa:float):
#     student_records=feild+","+str(reg_no)+","+name+","+fathername+","+str(cgpa)
#     file_output=open("student.txt",'a')
#     file_output.write(student_records)
#     file_output.close()
-------
# Display Records: Create a function to read and display all student records.
# def display_records():
#     file_input=open("student.txt",'r')
#     print(file_input)
#     file_input.close()
-------
# Search for a Record: Create a search function to find and display a specific student's record using their registration number.
# def search(registration_number):
#     file_input=open("student.txt",'r')
#     for line in file_input:
#         reg_n=line.split(",")[1]
#         if reg_n==registration_number:
#             print(line)
#             break
#     file_input.close()
-------
# Modify Records: Write a function to modify a student's record (e.g., update CGPA) using the registration number.










Delete Records: Write a function to delete a specific student record using the registration number.
Tasks for a file named course.txt:
Add Records: Create a function to add course details for students. Each student can have multiple course records.
Display Records: Write a function to display all courses of a specific student using registration number.
Search for a Record: Write a search function to find a specific course record for a student using the registration number and course code.
Modify Records: Write function to modify student's course details (e.g., update percentage or grades).
Delete Records: Implement a function to delete a specific course record of a student 

using the registration number and course code.
Instructions:Use appropriate error handling for file operations (e.g., file not found, invalid inputs).
Ensure data integrity across the files (e.g., a deleted student should also have their courses deleted).

Submit the following:
Python code.
Both text files namely student.txt and courses.txt with demo data.