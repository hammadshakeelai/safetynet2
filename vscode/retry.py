list=[7,5,57857,8,86,7568,7,865,46,8767,4,684464,444,4,8444448448,84,8,8]
flag=True
while len(list)>1:
    t=[]
    for i in list:
        if flag:
            t.append(i)
        flag=not flag
    list=t
print(list)