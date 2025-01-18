# Finding Smallest Postive Integer not in List
#my_list = [1, 3, 6, 4, 1, 2]
my_list = [1,2, 5, 3]
#my_list = [-1, -3]
for i in range(1,1000): # Maximum integer values is 1000
    LIST_MAI_HAI = False
    for j in my_list:
        if i == j:
            LIST_MAI_HAI = True
            break
    if not LIST_MAI_HAI:
        print(i)
        break
    
            