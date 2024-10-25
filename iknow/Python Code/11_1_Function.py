obtained_marks = 77
total_marks = 100

def calculate_percentage(obt_marks, tot_marks):
    if obt_marks > tot_marks:
        print("Invalid marks, total marks should be greater")
        return -1
    percentage = (obt_marks/tot_marks)*100
    return round(percentage,2)

def compute_pass_fail(percentage):
    if percentage > 100 or percentage < 0:
        print("Invalid percentage, should be from 0 to 100")
        return -1
    
    if percentage >= 60:
        return "Pass"
    else:
        return "Fail"

    
percentage_value = calculate_percentage(obtained_marks, total_marks)
print(percentage_value)
print(compute_pass_fail(percentage_value))

print("____Change Obtained Marks_____")
percentage_value = calculate_percentage(99, total_marks)
print(percentage_value)
print(compute_pass_fail(percentage_value))
