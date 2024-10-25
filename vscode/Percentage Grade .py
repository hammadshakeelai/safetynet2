def grader(Percentage_8):
    if Percentage_8>=90:
        return "your grade is A"
    if Percentage_8>=80:
        return "your grade is B"
    if Percentage_8>=70:
        return "your grade is C"
    if Percentage_8>=60:
        return "your grade is D"
    if Percentage_8>=50:
        return "your grade is E"
    else:
        return "your grade is F"
     
def Percentage_1(tot_marks, max_marks):
        return round((tot_marks/max_marks)*100, 2)

number_of_subjects=8
maximum_numbers_available=800
total_marks=0

runornot=str(input("do you want to find out your matric grade percentage, if so say yes :  "))
if runornot == "yes":
    for i in range(number_of_subjects):
        while True:
            x=int(input("enter your marks for one subject here :  "))
            if x>=0 and x<=100:
                total_marks+=x
                break
            else:
                print("Invalid marks input. Please enter a value between 0 and 100.")
                

    percentage=Percentage_1(total_marks,maximum_numbers_available)
    print("your fsc percentage is", percentage, "%")

    u=str(input("do you want to find out grade as well, if so say yes :     "))
    
    if u=="yes":
        grade=grader(percentage)
        print(grade)