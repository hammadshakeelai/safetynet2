# Sum the two distinct largest values in the List
my_list = [1, 20, 7, 2, 4, 7, 18, 3]
#my_list = [3, 3, 3, 3]

list_size = len(my_list)
biggest1st = 0
max_2 = 0
for i in range(list_size): # Maximum integer values is 1000
    if my_list[i] > biggest1st:
        max_2 = biggest1st
        biggest1st = my_list[i]

    elif my_list[i] > max_2 and my_list[i] != biggest1st:
        max_2 = my_list[i]

    elif biggest1st == max_2 and my_list[i] != max_2:
        max_2 = my_list[i]

if biggest1st == max_2:
    print(biggest1st)
else:
    print(biggest1st, max_2)
    print(biggest1st + max_2)