my_list = [-1, 9, 9, 3, 4, 5, 9, 7, 7 , 7  , 7 , 8 , 9, 9, -3]
k=0
for j in range(2):
    for i in range(1000,-1,-1): # Maximum integer values is 1000
        if i in my_list:
            j=i
            print(j)
            k=k+j
            break
    while i in my_list:
        my_list.remove(i)
print(k)