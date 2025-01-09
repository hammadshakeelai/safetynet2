'''
Syntax: [expression for item in iterable if condition]
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exp_list = [x**2 if x%2 == 0 else x for x in my_list]
print(exp_list)

## List Comprehension with Multiple Conditions
result = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(result)

## Nested List Comprehension
coordinates = [(x, y) for x in range(3) for y in range(2)]
print(coordinates)