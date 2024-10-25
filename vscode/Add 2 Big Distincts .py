my_list =[3,3,2]
max_value =my_list[0]
second_max_value =my_list[0]
for i in my_list:
    if i > max_value:
        second_max_value = max_value
        max_value = i
    elif second_max_value < i and i!=max_value or max_value == second_max_value and i != second_max_value:
        second_max_value = i
if max_value == second_max_value:
    print(0)
else:
    print(max_value, second_max_value)
    print(max_value + second_max_value)