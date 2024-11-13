def find_last_person():
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
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
find_last_person()

