# Calculate, use append, but print in reverse
num = 95

my_list = []
while(num > 0):
    binary_digit = num % 2
    my_list.append(binary_digit) # Appending digit will print digits in reverse
    num = num//2

size = len(my_list)
print("List Printing: ", end="")
for i in range(size): 
    print(my_list[i], end="") # Print in Reverse

print("\nReverse Printing: ", end="")
for i in range(size):
    print(my_list[size - (i + 1)], end="") # Print in Correct Order