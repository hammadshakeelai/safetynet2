my_list = [1, 3, 6, 4, 1, 2]
for i in range(len(my_list)):
    for j in my_list:
        if i!=j:
            j+=1
            break
print(j)
    