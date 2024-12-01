file_input = open("my_file.txt", 'r')
line = file_input.readline()
counter_odd = 0
counter_even = 0
while(line):
    num = int(line)
    if num % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    line = file_input.readline()

file_input.close()
print("Odd Count: ", counter_odd)
print("Even Count: ", counter_even)