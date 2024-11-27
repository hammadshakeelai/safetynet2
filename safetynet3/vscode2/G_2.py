list1 = [1, 2, 2]
list2 = [1, 1, 2,6,7,8]
#2 6 7 8
thirdlist=[]
n=len(thirdlist)
FLAG=False

for i in range(len(list1)):
    for j in range(len(list2)):
        flag=False
        if list1[i]==list2[j]:
            FLAG=True
        for p in range(len(list1)):
            if list2[j]==list1[p]:
                flag=True
        if flag:
            thirdlist.append(list2[j])
            flag=False
    if FLAG:
        thirdlist.append(list1[i])
        
        
    
            
            
print(thirdlist)