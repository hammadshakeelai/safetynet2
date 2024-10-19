# Finding Smalles Postive Integer not in List
#my_list = [1, 3, 6, 4, 1, 2]
my_list = [1, 2, 3]
#my_list = [-1, -3]
list_size = len(my_list)
for i in range(1, 1000): # Maximum integer values is 1000
    flag = False
    for j in range(list_size):
        if i == my_list[j]:
            flag = True
            break

    if not flag:
        print(i)
        break
    
            