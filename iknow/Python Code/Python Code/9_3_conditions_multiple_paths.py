# Two Path
marks = input("Enter Marks: ")
marks = float(marks)              # Convert to float value
marks = round(marks)              # Round to 0 decimal point

if marks >= 90:
    print("Outstanding")
    print("Your grade is A")

elif marks >= 80:
    print("Excellent")
    print("Your grade is B")

elif marks >= 70:
    print("Good")
    print("Your grade is C")

elif marks >= 60:
    print("Poor")
    print("Your grade is D")

else:
    print("Very Poor")
    print("Your grade is F")
