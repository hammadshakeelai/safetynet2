def find_last_person(n):
    my_list = [i for i in range(1, n+1)]
    print(my_list, "- Sword with", my_list[0])

    flag = True
    while(len(my_list) > 1):
        temp_list = []
        for item in my_list:
            if flag:
                temp_list.append(item)
            flag = not flag
        my_list = temp_list
        if flag:
            print(my_list, "- Sword with", my_list[0])
        else:
            print(my_list, "- Sword with", my_list[-1])
    return my_list[0]

print("The last person", find_last_person(10))