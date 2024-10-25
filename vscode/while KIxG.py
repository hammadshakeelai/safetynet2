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
    
number_of_subjects=8
counter=number_of_subjects
maximum_numbers_available=800
total_marks=0
runornot=str(input("do you want to find out your fsc grade percentage, if so say yes :  "))
if runornot=="yes":
    while counter!=0:
        counter-=1
        x=-1
        while x<0 or x>100:
            x=int(input("enter your marks for one subject here :  "))
            if x<0 or x>100:
                print("invalid marks input")
                break
            elif x>=0 and x<=100:
                total_marks=total_marks+x

    percentage=total_marks/maximum_numbers_available*100
    print(round(percentage, 2))

    u=str(input("do you want to find out grade as well, if so say yes :     "))
    
    if u=="yes":
        print(grader(percentage))