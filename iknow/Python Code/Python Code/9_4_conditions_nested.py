main_gate = input("University Gate is Open (Yes/yes): ")
class_room = input("Classroom is Open (Yes/yes): ")

if main_gate == "Yes" or main_gate == "yes":
     print("Welcome to University")
     if class_room == "Yes" or class_room == "yes":
          print("Welcome to Classroom")
     else:
          print("Classroom is closed")
else:
     print("University is closed")
