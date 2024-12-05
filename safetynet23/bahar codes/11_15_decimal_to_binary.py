# Calculate and Store in String.
num = 95

my_str = ""
while(num > 0):
    binary_digit = num % 2
    my_str = str(binary_digit) + my_str
    #my_str = my_str + str(binary_digit) # Adding new digit to right print in reverse
    num = num//2

print(my_str)