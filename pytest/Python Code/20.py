# Finding Smalles Postive Integer not in List
#my_list = [1, 3, 6, 4, 1, 2]
my_list = [1, 2, 3,6,5,4]
#my_list = [-1, -3]
list_size = len(my_list)#----------------------------COUNTS LIST NUMBERS
for i in range(1, 1000): # Maximum integer values is 1000#-----TRYS 1000 NUMBER 
    flag = False#?-------------------------------LOOP BREAKING STATEMENT
    for j in range(list_size):#----------------------RUN FOR AS MANY TIME AS THEIR ARE NUMBER IN LIST
        if i == my_list[j]:#-------------------------------CHECK IF 
            flag = True
            break

    if not flag:#???if not false -- print i and break loop
        print(i)
        break
    