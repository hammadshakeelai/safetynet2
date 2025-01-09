
## How to use the values of one list to create another list?
## Let solve it using convention method

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square = []
for item in my_list:
    list_square.append(item**2)
print(list_square)

#******************************************#
# Now, using list comprehension
## List comprehension is a compact representation to create lists 
## using a loop and optional condition in one line.
# OR
## A compact syntax for generating lists based on existing iterables (lists, ranges) 
## Applying a filtering conditions

'''
Syntax: [expression for item in iterable if condition]
Expression: The operation applied to each item in the iterable
Item: The variable representing each element in the iterable.
Iterable: The sequence of elements over which the comprehension iterates 
Condition: A filtering expression whether to included item in resulting list
'''

## Basic List Comprehension
list_square = [item**2 for item in my_list]
print(list_square)
