# Sum the two distince Maximum value in the List
my_list = [1, 7, 2, 4, 7, 18, 3]
my_list = [20, 7, 2, 4, 7, 18, 3]
#my_list = [3, 3, 3, 3]

list_size = len(my_list)
max_1 = my_list[0]
max_2 = my_list[0]
for i in range(list_size): # Maximum integer values is 1000
    if my_list[i] > max_1:
        max_2 = max_1
        max_1 = my_list[i]

    elif my_list[i] > max_2 and my_list[i] != max_1:
        max_2 = my_list[i]

    elif max_1 == max_2 and my_list[i] != max_2:
        max_2 = my_list[i]

if max_1 == max_2:
    print(0)
else:
    print(max_1, max_2)
    print(max_1 + max_2)