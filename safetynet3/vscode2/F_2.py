list1 = [0,1, 2, 2]
list2 = [1, 1, 2,6,7,8]
#2 6 7 8
thirdlist=[]
not_found=''
for i in range(len(list1)):
    if i not in list2:
        thirdlist.append(list1[i])
for i in range(len(list2)):
    if i not in list1:
        thirdlist.append(list2[i])
print(thirdlist)