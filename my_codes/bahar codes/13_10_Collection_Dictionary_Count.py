file = open("my_file.txt")
my_dict = {}
line = file.readline()
while(line):
    line = line.strip()
    if line in my_dict:
        #my_dict[line] = my_dict[line] + 1
        my_dict[line] += 1
    else:
        my_dict[line] = 1

    line = file.readline()

print(my_dict)
file.close()