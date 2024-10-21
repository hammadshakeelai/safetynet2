my_list =[20, 20, 7, 2, 4, 7, 18, 3, 2, 4, 7, 18, 3]
max_value =my_list[0]
second_max_value = float('-inf')
for i in my_list:
    if i > max_value:
        second_max_value = max_value
        max_value = i
    elif second_max_value < i and i!=max_value or max_value == second_max_value and i != second_max_value:
        second_max_value = i

if float("-inf") == second_max_value:
    print(0)
else:
    print(max_value, second_max_value)
    print(max_value + second_max_value)