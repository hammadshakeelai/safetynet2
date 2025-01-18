# Printing the n-th fibonacci number
total_num = int(input("Enter the number: "))
if (total_num) == 1:
     print(0)
elif (total_num) == 2:
     print(0, 1)

else:
     num1 = 0
     num2 = 1
     print(num1)
     print(num2)
     for i in range(total_num - 2): # First  two numbers are printed before
          num3 = num1 + num2
          
          num1 = num2
          num2 = num3
     
          print(num3)

