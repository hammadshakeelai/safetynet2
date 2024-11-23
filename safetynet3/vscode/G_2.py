# from G_1_ import indexC
# from G_1_ import N 
# first_list = [1, 2, 3]
# second_list = [1, 2]
# t

# first_list = [1, 2, 2, 3]
# second_list = [1, 2, 3]
# f

first_list = [1,2,2,2,1,2,2,2,2]
second_list = [1,1,2]
# t

match=0
seen=[]

for i in first_list:
    presencef=0
    for j in first_list:
        if i==j:
            presencef+=1
            seen.append(i)
        if presencef==1:
            match+=1
for i in second_list:
    presences=0
    for j in second_list:
        if i==j:
            presences+=1
            seen.append(i)
        if presences==1:
            match+=1

print(presences+presencef)