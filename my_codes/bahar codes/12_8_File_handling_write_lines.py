file_output = open("my_file.txt", 'w')
my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #Convert to String Values
file_output.writelines(my_list) # Does not add newlines automatically
#file_output.write(my_list) # This does not work
file_output.close()