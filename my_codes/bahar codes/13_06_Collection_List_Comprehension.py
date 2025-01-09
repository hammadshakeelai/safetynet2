'''
Syntax: [expression for item in iterable if condition]
'''
## List Comprehension with Condition
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_square = [x**2 for x in my_list if x % 2 == 0]
print(even_square)

## List Comprehension with Condition using range
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_square = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_square)