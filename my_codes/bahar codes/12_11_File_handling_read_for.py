file = open('my_file.txt')
counter = 0
for line in file:
    counter += 1
    print(counter, line, end="")