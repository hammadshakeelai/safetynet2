# Calculate and Print Values
num = 95
my_list = ""

while(num > 0):
    binary_digit = num % 2
    print(binary_digit, end="") # Issue is printing binary digits in reverse 
    num = num//2

print(my_list)