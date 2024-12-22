print("Welcome to Love Calculator")
name_1 = input("Enter the name of the First Person: ")
name_2 = input("Enter the name of the Second Person: ")
both_names = name_1 + name_2
lower_case = both_names.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
digit_1 = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
digit_2 = l + o + v + e

total_score = str(digit_1) + str(digit_2)
total_score = int(total_score)
if total_score<10 or total_score>90:
    print(f"Your Score is {total_score}, You Go togeather like coke and Mentos") 
elif total_score>=40 and total_score<=50:
    print(f"Your Score is {total_score}, You are Alright Togeather")
else:
    print(f"Your Score is {total_score}") 