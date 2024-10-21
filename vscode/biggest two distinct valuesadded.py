my_list = [20, 20]
max_value=-1000
second_max_value=-1000
for i in my_list:#checks all numbers
    if max_value<i :#agar i ka bara hai tuo
        second_max_value=max_value#chote max mai bara max ka dal do
        max_value=i#or bara max mai i ka  dal do
    elif second_max_value<i and i!=max_value:#agar i ka chote max se bara hai magar bara max se nai tuo chote max mai i ka dal do
        second_max_value=i

print(max_value+second_max_value)
        