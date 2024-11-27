# first_list = [1, 2, 2, 3]
# second_list = [1, 2, 3]

# first_list = [1, 2, 2, 2, 1]
# second_list = [1, 1, 2]

# first_list = [1, 2, 3]
# second_list = [1, 2]

first_list = [1, 2, 2, 2, 1, 2, 2, 2, 2]
second_list = [1, 1, 2]

if len(first_list)>=len(second_list):
    f1 = first_list.copy()
    f2 = second_list.copy()
    notmatch = 0
    for i in f1:
        if i in f2:
            f2.remove(i)  
        else:
            notmatch-=1
    print((len(f1)+notmatch)/len(f1)*100)
else:
    f2 = first_list.copy()
    f1 = second_list.copy()
    notmatch = 0
    for i in f1:
        if i in f2:
            f2.remove(i)  
        else:
            notmatch-=1
    print((len(f1)+notmatch)/len(f1)*100)