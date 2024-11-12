A = [21, 9, 3, 9, 8, 7, 3, 9, 7, 9, 9, 7, 21, 9, 8]
list = []
for num in A:
    if num in list:
        list.remove(num)
    else:
        list.append(num)
print(list[0])
