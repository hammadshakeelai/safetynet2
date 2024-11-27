list1 = [1, 2, 2]
list2 = [1, 1, 2,6,7,8]
#2 6 7 8
thirdlist=[]

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            continue
        for p in range(len(list1)):
            if list2[j]==list1[p]:
                continue
            thirdlist.append(list2[j])
            break
    thirdlist.append(list1[i])
       
print(thirdlist)