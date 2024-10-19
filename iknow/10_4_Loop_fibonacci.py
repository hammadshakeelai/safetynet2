# Printing fibonacci Series upto total number
total_num = int(input("Enter total number: "))
if (total_num) >= 1:
     print(0)
if (total_num) >= 2:
     print(1)

num1 = 0
num2 = 1
for i in range(total_num - 2): # First  two numbers are printed before
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3         