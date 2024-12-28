marks = float(input("Enter Marks: "))
marks = round(marks)
if marks >= 60:
     if marks >= 70:
          if marks >=80:
               if marks >= 90:
                    print("Outstanding")
                    print("Your Grade is A")
               else:
                    print("Excellent")
                    print("Your Grade is B")
          else:
               print("Good")
               print("Your Grade is C")
     else:
          print("Poor")
          print("Your Grade is D")
else:
     print("Very Poor")
     print("Your Grade is F")