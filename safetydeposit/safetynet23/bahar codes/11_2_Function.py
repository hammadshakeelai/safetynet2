obtained_marks = 90
total_marks = 130

def calculate_percentage(obt_marks, tot_marks):
    if obt_marks > tot_marks:
        print("Invalid marks, total marks should be greater")
        return -1
    percentage = (obt_marks/tot_marks)*100
    return round(percentage,2)

def compute_grade(percentage):
    if percentage > 100 or percentage < 0:
        print("Invalid percentage, should be from 0 to 100")
        return -1
    
    if percentage >= 90:
        return "Your grade is A"

    elif percentage >= 80:
        return "Your grade is B"

    elif percentage >= 70:
        return "Your grade is C"

    elif percentage >= 60:
        return "Your grade is D"

    else:
        return "Your grade is F"
    
percentage_value = calculate_percentage(obtained_marks, total_marks)
print(percentage_value)
print(compute_grade(percentage_value))

print("____Change Obtained Marks_____")
percentage_value = calculate_percentage(170, total_marks)
print(percentage_value)
print(compute_grade(percentage_value))
