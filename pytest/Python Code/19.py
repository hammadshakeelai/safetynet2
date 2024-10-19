# Finding Smalles Postive Integer not in List
# This program uses Python membership Operator (in)
#my_list = [1, 3, 6, 4, 1, 2]
#my_list = [1, 2, 3]
my_list = [-1, -3]
for i in range(1, 1000): # Maximum integer values is 1000
    if i not in my_list:
        print(i)
        break