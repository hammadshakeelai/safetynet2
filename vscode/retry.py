h=int(input("n : "))
list=[]
for i in range(1,h+1):
    list.append(i)
flag=True
while len(list)>1:
    t=[]
    for i in list:
        if flag:
            t.append(i)
        flag=not flag
    list=t
print(list)