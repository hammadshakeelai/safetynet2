file_input = open("my_file.txt", 'r')
line = file_input.read()

while(line):
    print(line, end="")
    line = file_input.read()

file_input.close()