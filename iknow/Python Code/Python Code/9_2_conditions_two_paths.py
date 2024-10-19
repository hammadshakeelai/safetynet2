# Two Path
marks = input("Enter Marks: ")
marks = float(marks)              # Convert to float value
marks = round(marks)              # Round to 0 decimal point
if marks >= 60:
    print("Congratualtion! ")
    print("You Passed")
else:
    print("Very Sad! ")
    print("You Failed")