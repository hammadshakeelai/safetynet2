first_list = [1,2,1]
second_list = [1,2,2,2,1]
match=0
for i in range(len(second_list)):
    for j in first_list:
        if second_list[i]==j:
            match+=1
            second_list.remove(second_list[i])
            first_list.remove(j)
print(match)