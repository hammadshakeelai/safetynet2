my_list = [20, 7, 2, 4, 18, 88, 20, 7, 2, 4, 18, 18, 20, 7, 2, 4, 18, 18, 20]
k=0
for j in range(2):#repeats two times
    for i in range(1000,-1,-1): # Maximum integer values is 1000
        if i in my_list:
            print(i)
            k=k+i
            break
    while i in my_list:
        my_list.remove(i)
print(k)
print(my_list)