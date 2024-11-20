# Calculate and Add to List
num = 95

my_list = []
while(num > 0):
    binary_digit = num % 2
    my_list.insert(0, binary_digit)
    #my_list.append(binary_digit) # Appending digit will print digits in reverse
    num = num//2

print(my_list)